"""
Seq Separator Module
-------------------------------------------------------------------------------
PURPOSE
-------------------------------------------------------------------------------
This module takes a nucleotide sequence input and separates the sequence into fixed-length blocks.
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


from SeqKitSTP.modules.sequence_processing import clean_sequence, validate_sequence


def block_sequence(sequence, block_size=10):
    """
    Split a nucleotide sequence into fixed-length blocks.

    Parameters
    ----------
    sequence : str
        Input nucleotide sequence
    block_size : int
        Length of each block (default = 10)

    Returns
    -------
    list
        List of sequence blocks
    """
    
    #validate block_size
    if not isinstance(block_size, int):
        logger.error("Block size must be an integer")
        raise TypeError("Block size must be an integer")
    
    if block_size <= 0:
        logger.error("Block size must be greater than 0")
        raise ValueError("Block size must be greater than 0")

    logger.debug("Block size validated: %s", block_size)
    
    cleaned_sequence = clean_sequence(sequence)

    # this function validates the cleaned sequence
    validate_sequence(cleaned_sequence)
    
    if block_size > len(cleaned_sequence):
        logger.warning("Block size is larger than sequence length. Returning entire sequence as one block.")
    
        return [cleaned_sequence]
    
    logger.info("Splitting sequence into blocks of size %s...", block_size)

    #creates empty list
    block_sequence_list = []

    for i in range(0, len(cleaned_sequence), block_size):
        #creates blocks of sequence based on block size
        chunks = cleaned_sequence[i : i + block_size]
        #append blocks to list
        block_sequence_list.append(chunks)

    logger.debug("Block sequence: %s", block_sequence_list)

    return block_sequence_list



sequence = input("Enter a raw DNA sequence: ")
block_size = int(input("Enter block size (e.g. 10): "))
validate_sequence(sequence)
print(block_sequence(sequence, block_size))

