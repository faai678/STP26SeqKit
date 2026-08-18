
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

import requests
from SeqKitSTP.code_examples import genenames_requests

"""
Take a gene symbol from the command line and also a reference sequence source (refseq or ensembl)
Fire a request to the genenames.org API to get the up-to-date gene symbol, HGNC gene ID and MANE Select transcript for the requested reference sequence source
Fire a request to the relevant API to get the transcript sequence, CDS start and CDS end for the transcript, and if possible the translation ID (NP_ or ENSP)
Use your functions to transcribe and translate the transcript record
Create GenBank-formatted files for the cDNA transcript, RNA transcript and protein sequences
Cover with tests!!!

"""



def main(gene_symbol, ref_source):
    logger.info("Starting request for gene symbol:%s from source:%s", gene_symbol, ref_source)
    gene_info_output = genenames_requests.fetch_gene_info(gene_symbol)

    if ref_source.lower() == "r":
        for transcript in gene_info_output.get("MANE_Select", []):
            if transcript.startswith("NM_"):
                refseq_transcript_id = transcript
                break
            else:
                refseq_transcript_id = None
                logger.warning("No MANE Select Refseq transcript found for gene symbol: %s", gene_symbol)

    return gene_info_output, refseq_transcript_id



gene_symbol = input("Enter a gene symbol: ")
ref_source = input("Enter reference sequence source (R for RefSeq, E for Ensembl): ")
test_one = main(gene_symbol, ref_source)
print(test_one)

