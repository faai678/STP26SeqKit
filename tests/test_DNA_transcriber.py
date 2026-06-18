
import pytest
from SeqKitSTP.modules import DNA_transcriber
from SeqKitSTP.modules import sequence_processing
from SeqKitSTP.modules.DNA_transcriber import SequenceError

# Sequences derived from RefSeq record:
# https://www.ncbi.nlm.nih.gov/nuccore/NM_016274.6
# Note: this sequence intentionally contains whitespace and newlines
# to simulate real-world biological data formatting
sequences = {
    "dna": """
            ACAGCGCACCGGGCCGGGGGAGCGGCCGCGCTGGGCCGGGCGGGCGGGTGGCGGGGGTGCGCTCGGGGAC
            CCGGGCCGCGTGGGCGCCGGGATGGAGGGCGCCAAGGGGCGGGGAGCGGGCGTGCGTGTGTGTGCGAGTG
            CGAATGCGAGGGAGGCCGGCCTTGAGTGAAACCGGAGCTACAAAGAAGGGGAGAGTCCGGGAGCGGGAGG
            GCGCGAGGGAGGAGCGGCGGCGCCGGGGCAGCTCCGACGCCCTCCCGCGGGGAAGGAGCCCCCGCGGTGC
            CGCCGAGGCCCCGACGCGGGGCCGCCCCTCGGCTCGCCGCCCCGCGCCCGCGCCCGCTGGGAATGATGAA
            GAAGAACAATTCCGCCAAGCGGGGACCTCAGGATGGAAACCAGCAGCCTGCACCGCCCGAGAAGGTCGGC
            TGGGTCCGGAAATTCTGCGGGAAAGGGATTTTCAGGGAGATTTGGAAAAACCGCTATGTGGTGCTGAAAG
            GGGACCAGCTCTACATCTCTGAGAAGGAGGTAAAAGATGAGAAAAATATTCAAGAGGTATTTGACCTGAG
            TGACTATGAGAAGTGTGAAGAGCTCCGGAAGTCCAAGAGCAGGAGCAAGAAAAATCATAGCAAGTTTACT
            CTTGCCCACTCCAAACAGCCCGGTAACACGGCACCCAACCTGATCTTCCTGGCAGTGAGTCCAGAAGAGA
            AGGAATCGTGGATCAATGCCCTCAACTCTGCCATCACCCGAGCCAAGAACCGTATCTTGGATGAGGTCAC
            CGTTGAGGAGGACAGCTATCTTGCCCATCCCACTCGAGACAGGGCAAAAATCCAGCACTCCCGCCGCCCC
            CCAACAAGGGGACACCTAATGGCTGTGGCTTCCACCTCTACCTCGGATGGGATGCTGACCTTGGACTTGA
            TCCAAGAGGAAGACCCTTCCCCTGAGGAACCAACCTCTTGTGCTGAGAGCTTTCGGGTTGACCTGGACAA
            GTCTGTGGCCCAGCTGGCAGGGAGCCGGCGGAGAGCGGACTCAGACCGCATCCAGCCCTCCGCAGACCGG
            GCAAGCAGTCTCTCCCGACCTTGGGAAAAAACAGACAAAGGGGCCACCTACACCCCCCAGGCACCCAAGA
            AGTTGACGCCCACAGAGAAAGGCCGCTGCGCCTCCCTGGAGGAGATCCTATCTCAGCGGGATGCTGCCTC
            TGCCCGCACCCTCCAGCTGCGGGCTGAGGAACCCCCAACCCCTGCCCTCCCCAACCCGGGGCAGCTGTCC
            CGGATCCAGGACCTGGTAGCAAGGAAACTGGAGGAGACTCAGGAGCTTCTGGCAGAGGTTCAGGGACTGG
            GAGATGGGAAGCGAAAGGCCAAGGACCCCCCTCGGTCTCCGCCGGATTCTGAGTCAGAGCAGCTGCTGCT
            GGAGACGGAACGGCTGCTGGGAGAGGCATCATCGAATTGGAGCCAGGCAAAGAGGGTGCTGCAGGAGGTC
            AGGGAGCTGAGAGACCTGTACAGACAGATGGACCTGCAGACCCCGGACTCCCACCTCAGACAGACCACCC
            CGCACAGTCAGTACCGGAAGAGCCTGATGTGAGGGCAGGGTGGGGTCTGGAACTTGTCGGGTTGGACAGA
            CTCTTATCTCCGTGTTGCTGGATAAAGCTTTTTTATTTACCTCAATCAAAAAAAGAAAACAAAAATGAAC
            TCATTGCTCTTGCTGATGCCTGACCCCACTACAACCCTTATTGCCCCACCTACTTTCCATATGCCCCTCG
            TATGCCCCTCAGGTTTGAGGAAGTGACCCCGCAGCAGTAGCAGGAAGTTTTTACCCAGCCAGAGAGAGAG
            AAGGCACGGTAAAGACACAGTCTGACCACTCCACACACCGCCCGCCCCCAAGACGGCACAGGGAGTCCAC
            TGCTGCTCCCAAGGATACAGTGGGCTTCTAAGCTTAGAGCGGGAGGGGGATGAGGATGTTTTCTGTTATG
            TCCCACCCCAGGCCTTCAGTTTGAGGGTGAAGTTTCAGCTGCCCAACTCTAGTTGTAGGGATGTGGAGGC
            CAGTGTCACCTGTCCGTGCACATGGAAGTGAAATTTATCCCAGCCCTGAGGAGGATTTGTGGAATTAAAA
            TCTCCCCAGCCAGA
            """
}

def test_transcribe_dna():
    """
    Test that a valid DNA sequence is correctly transcribed to RNA.

    Key learning points:
    - Input contains whitespace → function should clean it
    - T (thymine) should be replaced with U (uracil)
    - Output should be lowercase RNA
    """

    transcribed_dna = DNA_transcriber.dna_transcribe(sequences["dna"])

    # Construct expected result:
    # 1. Replace T with U
    # 2. Convert to lowercase
    # 3. Remove whitespace
    transcribed_sequence = "".join(
        sequences["dna"].replace("T", "U").lower().split()
    )

    assert transcribed_dna == transcribed_sequence



def test_transcribe_rna_fails():
    """
    Test that transcribing RNA raises an error.

    Key learning point:
    - The function expects DNA (with T), not RNA (with U)
    - Good validation should reject incorrect biological input
    """

    transcribed_dna = DNA_transcriber.dna_transcribe(sequences["dna"])

    # Attempting to transcribe RNA again should fail
    with pytest.raises(SequenceError):
        DNA_transcriber.dna_transcribe(transcribed_dna)



def test_transcribe_invalid_character():
    """
    Test that invalid DNA characters raise an error.
    """

    clean_dna = "".join(sequences["dna"].split())
    
    # here we areintroducing x as invalid character
    invalid_dna = clean_dna[:-1] + "X"

    with pytest.raises(SequenceError):
        DNA_transcriber.dna_transcribe(invalid_dna)




def test_transcribe_lowercase_fails():
    """
    Test that lowercase DNA sequences are rejected.
    """

    clean_dna = "".join(sequences["dna"].split()).lower()

    with pytest.raises(SequenceError):
        DNA_transcriber.dna_transcribe(clean_dna)

