"""
Sequence Processing Module
-------------------------------------------------------------------------------
PURPOSE
-------------------------------------------------------------------------------
This module takes a nucleotide sequence input, clean and validates the sequence.
Expected input: a string of nucleotides (e.g. "ATGCGTACGTAGCTAG")
Expected output: a string of nucleotides separated into blocks of desired length 
-------------------------------------------------------------------------------
INPUT
-------------------------------------------------------------------------------
- Sequence input: string containing nucleotides in text format file??
- Desired block length: integer (e.g. 10 for blocks of 10 nucleotides)
- Formats of nucleotide for different types of sequence (e.g. DNA, RNA)??
-------------------------------------------------------------------------------
OUTPUT
-------------------------------------------------------------------------------
- A list of nucleotides separated into blocks of the specified length
# - Output saved in txt file (put this in main.py)
-------------------------------------------------------------------------------

"""

import logging
logger = logging.getLogger(__name__)


def clean_sequence(sequence):
    """
    Clean the input sequence by removing whitespace and converting to lowercase.

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
    #remove whitespace, convert to lowercase, and remove spaces and newlines
    cleaned_sequence = sequence.strip().lower().replace(" ", "").replace("\n", "")
    
    logger.info("Cleaned sequence: %s", cleaned_sequence)
    
    return cleaned_sequence


def validate_sequence(cleaned_sequence):
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

    logger.info("Validating sequence...")

    # Check type
    if not isinstance(cleaned_sequence, str):
        logger.error("Sequence must be a string")
        raise TypeError("Sequence must be a string")

    # Check empty
    if not cleaned_sequence:
        logger.error("Sequence is empty")
        raise ValueError("Sequence cannot be empty")

    # Define valid characters
    valid_nucleotides = {"a", "t", "g", "c", "n"}

    # Check each character
    for char in cleaned_sequence:
        if char not in valid_nucleotides:
            logger.error("Invalid character found: %s", char)
            raise ValueError(
                "Sequence contains invalid characters. Only a, t, g, c, n allowed."
            )

    logger.info("Sequence validation passed")