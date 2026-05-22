"""
GenBank Style Generator Module
-------------------------------------------------------------------------------
PURPOSE
-------------------------------------------------------------------------------
This module takes a nucleotide sequence and formats it in Genbank Style
NOTE: Genbank style is 60 nucleotides per line, grouped into blocks of 10
-------------------------------------------------------------------------------
INPUT
-------------------------------------------------------------------------------
- Sequence input: string containing nucleotides
- Block length: 10
-------------------------------------------------------------------------------
OUTPUT
-------------------------------------------------------------------------------
- A string of nucleotides separated into 6 blocks of 10 nucleotides per line
- Lines numbered at the start of each line, according to sequence position
# - Output saved in txt file (put this in main.py)
-------------------------------------------------------------------------------

"""
import logging
logger = logging.getLogger(__name__)

#importing pre-defined functions instead of repeating code
from SeqKitSTP.modules.sequence_chunker import clean_sequence, validate_sequence

def format_genb_sequence(sequence):
    """
    Convert a sequence into GenBank format.

    Parameters
    ----------
    sequence : str
        Input nucleotide sequence

    Returns
    -------
    str
        Sequence formatted in GenBank style
    """
    logger.info("Formatting sequence in GenBank style...")
    
    # Clean the input sequence
    cleaned_sequence = clean_sequence(sequence)

    #Validate the cleaned sequence
    validate_sequence(cleaned_sequence)
    
    # Creates a genb_seq with empty string.
    genb_seq = ""

    for i in range(0, len(cleaned_sequence), 60):
        # create lines of 60 nucleotides
        line_seq = cleaned_sequence[i : i + 60]
        
        # calculate position for line number
        line_number = i + 1

        #split 60 nucleotides into blocks of 10
        blocks = []
        for j in range(0, len(line_seq), 10):
            chunk = line_seq[j : j + 10]    
            blocks.append(chunk)

        # join blocks with spaces
        formatted_blocks = " ".join(blocks)

        #add line_number to formatted blocks. line_number 9-char field(human_genome size) right aligned for Genbank format
        formatted_line = f"{line_number:>9} {formatted_blocks}"

        # append formatted_line to genb_seq with new line
        genb_seq += formatted_line + "\n"

    logger.debug("Formatted GenBank sequence: \n %s" , genb_seq)
    
    return genb_seq
