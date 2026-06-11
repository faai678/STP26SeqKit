"""
Sequence Processing Module
-------------------------------------------------------------------------------
PURPOSE
-------------------------------------------------------------------------------
This module takes a nucleotide sequence input, clean and validates the sequence.
Expected input: a string of nucleotides (e.g. "ATGCGTACGTAGCTAG")
Expected output: a cleaned string of nucleotides remove whitespace and remove spaces and newlines
Only valid for canonical DNA sequences (A, T, G, C in upper/lower case)
-------------------------------------------------------------------------------
INPUT
-------------------------------------------------------------------------------
- Sequence input: string containing nucleotides in text format file??
- Formats of nucleotide for different types of sequence (e.g. DNA, RNA)??
-------------------------------------------------------------------------------
OUTPUT
-------------------------------------------------------------------------------
- A list of nucleotides separated into blocks of the specified length
# - Output saved in txt file (put this in main.py)
-------------------------------------------------------------------------------

"""

import logging

from SeqKitSTP.modules.DNA_transcriber import SequenceError
logger = logging.getLogger(__name__)


def clean_sequence(sequence):
    """
    Clean the input sequence by removing whitespace.

    Parameters
    ----------
    sequence : str
        Input nucleotide sequence

    Returns
    -------
    str
        Cleaned sequence
    """
    logger.info("Cleaning input sequence...")
    #remove whitespace and remove spaces and newlines
    cleaned_sequence = "".join(sequence.split())
    
    logger.info("Cleaned sequence: %s", cleaned_sequence)
    
    return cleaned_sequence


def validate_sequence(sequence, valid_bases, sequence_type):
    """
    Validate that the sequence contains only valid nucleotide characters.

    Parameters
    ----------
    sequence : str
        Cleaned nucleotide sequence

    Returns
    -------
    None
        Raises an error if invalid
    """

    logger.info("Validating sequence...",sequence_type)

    # Check type
    if not isinstance(sequence, str):
        logger.error("Sequence must be a string")
        raise TypeError("Sequence must be a string")

    # Check empty
    if not sequence:
        logger.error("Sequence is empty")
        raise ValueError("Sequence cannot be empty")
    # Loop through each base in the sequence.
    # enumerate() gives both the position (pos) and the base itself.
    # start=1 makes positions biologically intuitive (1-based indexing).
    for pos, base in enumerate(sequence, start=1):
         # Check that each base is one of the allowed DNA nucleotides.
        if base not in [valid_bases]:
            # Raise a detailed error including the invalid base and its position.
            raise SequenceError(f"Non-DNA base {base} at position {pos}")

    logger.info("Sequence validation passed")