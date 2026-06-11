"""
DNA transcriber module for SeqKitSTP
-------------------------------------------------------------------------------
PURPOSE
-------------------------------------------------------------------------------
This module takes a DNA sequence and transcribes it into RNA
-------------------------------------------------------------------------------
INPUT
-------------------------------------------------------------------------------
- Sequence input: string containing nucleotides
- Transcription rules: convert T to U , lowercase
-------------------------------------------------------------------------------
OUTPUT
-------------------------------------------------------------------------------
- A string of nucleotides in lowercase to show RNA sequence and T is replaced with U
-------------------------------------------------------------------------------
"""


import logging

# Create a logger for this module.
# __name__ ensures the logger is tied to this file's namespace.
logger = logging.getLogger(__name__)

from sequence_processing import clean_sequence, validate_sequence  # Import specific functions for clarity

# Custom exception class for sequence-related errors.
# This allows us to raise meaningful, domain-specific errors
# instead of using generic Python exceptions.
class SequenceError(Exception):
    pass

def dna_transcribe(dna_sequence):
    """
    Transcribe a DNA sequence to RNA.

    Parameters
    ----------
    dna_sequence : str
        DNA sequence to transcribe.

    Returns
    -------
    str
        Transcribed RNA sequence.
    """
    # Log the incoming sequence for traceability/debugging.
    logger.info("Transcribing DNA: %s", dna_sequence)

    # Remove all whitespace (spaces, tabs, newlines).
    # .split() breaks the string on whitespace -> list of chunks
    # "".join(...) recombines them into a single continuous sequence
    dna_sequence_cleaned = clean_sequence(dna_sequence)

    # If the cleaned sequence differs, warn the user.
    # This helps highlight that input formatting was adjusted.
    if dna_sequence_cleaned != dna_sequence:
        logger.warning("Whitespace removed from DNA sequence")

    # Validate that the cleaned sequence is valid DNA
    # (only A, T, G, C and uppercase).
    validate_sequence(dna_sequence_cleaned)

    # Log the cleaned sequence before transcription.
    logger.info("DNA sequence validation successful.")
    


    # Perform transcription:
    # Replace thymine (T) with uracil (U) to simulate RNA
    # Convert to lowercase to indicate RNA output convention
    rna_sequence = dna_sequence_cleaned.replace("T", "U").lower()

    # Log the resulting RNA sequence.
    logger.info("Transcribed RNA: %s", rna_sequence)

    # Return the final RNA sequence
    return rna_sequence
