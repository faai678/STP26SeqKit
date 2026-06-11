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
    "UUU": "F", "UUC": "F",

    # Leucine
    "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",

    # Isoleucine
    "AUU": "I", "AUC": "I", "AUA": "I",

    # Methionine (START)
    "AUG": "M",

    # Valine
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",

    # Serine
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "AGU": "S", "AGC": "S",

    # Proline
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",

    # Threonine
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",

    # Alanine
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",

    # Tyrosine
    "UAU": "Y", "UAC": "Y",

    # Histidine
    "CAU": "H", "CAC": "H",

    # Glutamine
    "CAA": "Q", "CAG": "Q",

    # Asparagine
    "AAU": "N", "AAC": "N",

    # Lysine
    "AAA": "K", "AAG": "K",

    # Aspartic Acid
    "GAU": "D", "GAC": "D",

    # Glutamic Acid
    "GAA": "E", "GAG": "E",

    # Cysteine
    "UGU": "C", "UGC": "C",

    # Tryptophan
    "UGG": "W",

    # Arginine
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGA": "R", "AGG": "R",

    # Glycine
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",

    # STOP codons
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP"
}
def rna_translate(rna_sequence):
    """
    Translate an mRNA sequence to a protein sequence.
    """
    logger.info("Translating RNA: %s", rna_sequence)

#validate input RNA sequence
    logger.info("Validating sequence...",sequence_type)
    valid_bases = ["A", "U", "C", "G", "a", "u", "c", "g"]
    sequence_type = "RNA"
    rna_sequence_cleaned = sequence_processing.clean_sequence(rna_sequence)
    sequence_processing.validate_sequence(rna_sequence_cleaned, valid_bases, sequence_type)

    # Ensure uppercase
    rna_sequence_upper = rna_sequence_cleaned.upper()

    protein = []
    start_found = False

    # Iterate in codons (3 bases)
    for i in range(0, len(rna_sequence_upper), 3):
        codon = rna_sequence[i:i+3]

        if len(codon) < 3:
            break  # ignore incomplete codon at end

        amino_acid = GENETIC_CODE.get(codon)

        if amino_acid is None:
            raise ValueError(f"Invalid codon: {codon}")

        # Wait for start codon
        if not start_found:
            if codon == "AUG":
                start_found = True
                protein.append("M")
            continue

        # Stop codon
        if amino_acid == "STOP":
            break

        protein.append(amino_acid)

    result = "".join(protein)
    logger.info("Protein sequence: %s", result)

    return result
