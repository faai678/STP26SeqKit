"""
mRNA Translator to Protein Module
-------------------------------------------------------------------------------
PURPOSE
-------------------------------------------------------------------------------
This module takes an mRNA sequence and translates it into a protein sequence
NOTE: Translation follows standard genetic code with start and stop codons
-------------------------------------------------------------------------------
INPUT
-------------------------------------------------------------------------------
- mRNA sequence: string containing nucleotides
- Genetic code: dictionary mapping codons to amino acids
-------------------------------------------------------------------------------
OUTPUT
-------------------------------------------------------------------------------
- A string of amino acids representing the translated protein sequence
- Start and stop codons are handled appropriately
-------------------------------------------------------------------------------
"""

import logging

logger = logging.getLogger(__name__)
from SeqKitSTP.modules import sequence_processing 

# Standard genetic code
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

def rna_translate(rna_sequence):
    """
    Translate an mRNA sequence to a protein sequence.
    """
    logger.info("Translating RNA: %s", rna_sequence)

# clean and validate input RNA sequence

    valid_bases = ["a", "u", "c", "g"]
    sequence_type = "RNA"
    logger.info("Cleaning and validating %s sequence...",sequence_type)

    rna_sequence_cleaned = sequence_processing.clean_sequence(rna_sequence)
    sequence_processing.validate_sequence(rna_sequence_cleaned, valid_bases, sequence_type)

    #create empty protein list
    protein = []
    start_found = False

    # Iterate in codons (3 bases)
    for i in range(0, len(rna_sequence_cleaned), 3):
        codon = rna_sequence_cleaned[i:i+3]

        if len(codon) < 3:
            break  # ignore incomplete codon at end

        amino_acid = GENETIC_CODE.get(codon)

        if amino_acid is None:
            logger.error("Invalid codon: %s", codon)
            raise ValueError(f"Invalid codon: {codon}")

        # Wait for start codon
        if not start_found:
            if codon == "aug":
                start_found = True
                protein.append("M")
            continue

        # Stop codon
        if amino_acid == "STOP":
            break

        protein.append(amino_acid)

        if not start_found:
            logger.error("No start codon found in the sequence")
            raise ValueError("No start codon found in the sequence")
    # joins aminoacids list into string
    result = "".join(protein)
    logger.info("Protein sequence: %s", result)

    return result
