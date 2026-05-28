"""
SeqKitSTP application
----------------------------------------------
PURPOSE
----------------------------------------------
This is the main entry point for the SeqKitSTP application.

It is responsible for:

✔ Initialising logging once at startup
✔ Importing and coordinating application modules
✔ Running the sequence formatting workflow

In this project, the workflow is:

raw DNA sequence
    → chunk separated into fixed-size blocks
    → group blocks into GenBank-format rows
    → render printable GenBank sequence text

-----------------------------------------------
LOGGING DESIGN
-----------------------------------------------
Logging is configured once at startup in this main module, and then used throughout the application modules.
In other words, logging is configured centrally.

Why? 
logging.config.dictConfig(...) replaces existing logging
configuration. Calling it repeatedly can:

→ reset handlers
→ duplicate output
→ create inconsistent behaviour

Therefore:

✔ setup_logging() is called once at startup
✔ modules do NOT configure logging themselves

----------------------------------------
HOW MODULE LOGGERS WORK
----------------------------------------

After logging is configured:

- modules use:
      logging.getLogger(__name__)

- Python builds a logger hierarchy from module paths

Example:
      SeqKitSTP.modules.chunk_text

Those module loggers then inherit configuration from
the root logger.

That means:

✔ shared handlers
✔ shared formatter
✔ shared log level

So we do not pass logger objects around and we do not
configure logging inside individual modules.

----------------------------------------
SUMMARY
----------------------------------------

Configure once → application start
Use __name__ → automatic logger hierarchy
Import modules normally → they inherit logging behaviour

extra note:  Always run your program from the directory above your package
"""

# ------------------------------
# Step 1 - import logging setup
# ------------------------------
"""
Logging must be initialised before application code runs
This ensures all later logger calls use the same
configuration.

"""

from SeqKitSTP.logger import setup_logging
import logging
# Configure logging once for the whole application.
# This is intentionally done at module startup.
setup_logging()

# Create a logger for this module.
# __name__ will usually be:
# "main" when run directly
# or module path when imported elsewhere
logger = logging.getLogger(__name__)

# --------------------------------------------------
# Step 2 - import application modules
# --------------------------------------------------
"""
These modules create their own loggers using __name__.

Because setup_logging() has already run, their loggers
will inherit the configured handlers, levels and formatters.
"""

from SeqKitSTP.modules import seq_separator, genb_format_generator

# --------------------------------------------------
# Step 3 - main application function
# --------------------------------------------------
def main(dna_string):
    """
    Main function to run the SeqKitSTP application.
    This function orchestrates the sequence formatting workflow.
    Convert a raw DNA sequence into printable genbank format text.

    Explain workflow:
        1. Remove whitespace
        2. Convert to lowercase
        3. Split into 10-base chunks
        4. Group into rows of 6 blocks (60 bases per row)
        5. Add GenBank-style left-hand coordinates

    parameters: input of dna string (str):
        Raw DNA sequence input. May contain whitespace,
        line breaks or wrapped sequence text.
    
    Returns:
    str:
        Formatted GenBank-style sequence block.
    """

    # Record the first transformation stage.
    #logger.info("Split into blocks")

    # chunk_string_to_blocks() performs:
    #
    # - whitespace removal
    # - lowercase conversion
    # - chunk into 10-base blocks
    # - 6 blocks per printed row
    #
    # Example output:
    # [
    #     ['atgc...', '....'],
    #     ['....']
    # ]
    logger.info("Starting sequence formatting workflow")
    return genb_format_generator.format_genb_sequence(dna_string)

# --------------------------------------------------
# Script entry point
# --------------------------------------------------
"""
This block runs only when the file is executed directly.

It does not run when this module is imported elsewhere.
"""

if __name__ == "__main__":

    # Example DNA sequence.
    # Multi-line input is acceptable because whitespace
    # is removed by chunk_string_to_blocks().
    dna_string = input("Enter a raw DNA sequence: ")

    """
        GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGC
        CTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAA
        GAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGG
        AACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAA
        AGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTT
        AGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAA
        ACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCA
        AAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAA
        ACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAAC
        CTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTA
        TTGCAGTGTGGGAGATCAAG
        """  

    # Run the formatting pipeline and print the result.
    print(main(dna_string))


