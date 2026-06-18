import pytest
from SeqKitSTP.modules import mRNA_translator
from SeqKitSTP.modules import sequence_processing
from SeqKitSTP.modules.mRNA_translator import SequenceError


GENETIC_CODE = {
    # Phenylalanine
    "uuu": "F", "uuc": "F",

    # Leucine
    "uua": "L", "uug": "L",
    "cuu": "L", "cuc": "L", "cua": "L", "cug": "L",

    # Isoleucine
    "auu": "I", "auc": "I", "aua": "I",

    # Methionine (START)
    "aug": "M",

    # Valine
    "guu": "V", "guc": "V", "gua": "V", "gug": "V",

    # Serine
    "ucu": "S", "ucc": "S", "uca": "S", "ucg": "S",
    "agu": "S", "agc": "S",

    # Proline
    "ccu": "P", "ccc": "P", "cca": "P", "ccg": "P",

    # Threonine
    "acu": "T", "acc": "T", "aca": "T", "acg": "T",

    # Alanine
    "gcu": "A", "gcc": "A", "gca": "A", "gcg": "A",

    # Tyrosine
    "uau": "Y", "uac": "Y",

    # Histidine
    "cau": "H", "cac": "H",

    # Glutamine
    "caa": "Q", "cag": "Q",

    # Asparagine
    "aau": "N", "aac": "N",

    # Lysine
    "aaa": "K", "aag": "K",

    # Aspartic Acid
    "gau": "D", "gac": "D",

    # Glutamic Acid
    "gaa": "E", "gag": "E",

    # Cysteine
    "ugu": "C", "ugc": "C",

    # Tryptophan
    "ugg": "W",

    # Arginine
    "cgu": "R", "cgc": "R", "cga": "R", "cgg": "R",
    "aga": "R", "agg": "R",

    # Glycine
    "ggu": "G", "ggc": "G", "gga": "G", "ggg": "G",

    # STOP codons
    "uaa": "STOP",
    "uag": "STOP",
    "uga": "STOP"
}


# aug uac aau gcc aug gag auc agc gag gac cgg auc agc uaa
#  M   Y   N   A   M   E   I   S   E   D   R   I   S  STOP 




def test_translate_rna():
    """
    Test that a valid RNA sequence is correctly translated into protein sequence.

    Key learning points:
    - Translation begins at AUG
    - Codons translated into aminoacids 
    - Translation stops at the first stop codon
    """
    rna = "auguacaaugccauggaaauaagcgaggaccggaucagcuaa"
    rna_expected_output = "MYNAMEISEDRIS"
    
    
    translated_rna = mRNA_translator.rna_translate(rna)
    assert translated_rna == rna_expected_output 





def test_translate_stops_at_stop_codon():
    """
    Test that translation stops at the first stop codon.

    """

    # added additionaal stop codon after MYNAME
    rna_extra_stop = "auguacaaugccauggaaugaauaagcgaggaccggaucagcuaa"
    rna_extra_stop_output = "MYNAME"
    
    translated_rna = mRNA_translator.rna_translate(rna_extra_stop)
    assert translated_rna == rna_extra_stop_output

def test_translate_invalid_character():
    """
    Test that invalid RNA characters raise an error.

    """

    rna_invalid = "uaguacaaugccuaggaaauaagcgaggaccggaucagcuxaa"  # 'x' is invalid

    with pytest.raises(SequenceError):
        mRNA_translator.rna_translate(rna_invalid)

def test_translate_dna_fails():
    """
    Test that DNA sequences fail translation.

    """
    dna = "atgatgatg"

    with pytest.raises(SequenceError):
        mRNA_translator.rna_translate(dna)

def test_translate_no_start_codon():
    """
    Test that translation fails without a start codon.

    """
    rna_no_start = "uacaaugccgaaauaagcgaggaccggaucagcuaa"

    with pytest.raises(ValueError):
        mRNA_translator.rna_translate(rna_no_start)