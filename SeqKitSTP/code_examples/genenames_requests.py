"""
Extend your API calls to make a request to the genenames.org API (https://www.genenames.org/help/rest/Links to an external site.)

Build a main.py to orchestrate the following functional workflow

    Take a gene symbol from the command line and also a reference sequence source (refseq or ensembl)

    Fire a request to the genenames.org API to get the: 
        up-to-date gene symbol
        HGNC gene ID
        MANE Select transcript 
    for the requested reference sequence source

    Fire a request to the relevant API to get the: from refseq and ensembl
        transcript sequence
        CDS start
        CDS end
        translation ID (NP_ or ENSP)
    for the transcript

    Use your functions to transcribe and translate the transcript record

    Create GenBank-formatted files for the cDNA transcript, RNA transcript and protein sequences

    Cover with tests!!!

Input: gene symbol + Refseq/Ensembl source

Output:
dict{
    up to date symbol
    HGNC gene ID
    MANE Select transcript ID, if not use mane plus clinical, if not use canonical, if not say N/A
    transcript sequence ID
    transcript sequence in Genbank format
    RNA sequence in Genbank format
    translation ID
    protein sequence in Genbank format
}


"""
import requests
import json

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

url = "https://rest.genenames.org/"


def fetch_gene_info(gene_symbol):
    """
    Fetch gene info from genenames.orgAPI

    use url
    determine path and parameters
    use FETCH

    input: gene symbol

    output:
    up to date symbol
    HGNC ID
    MANE Select
    """
    path = "fetch/symbol/" + gene_symbol

    genenames_response = requests.get(url + path, headers={"Accept": "application/json"})

    genenames_info = genenames_response.json()

    extracted_dict = {
     "up_to_date_symbol": genenames_info["response"]["docs"][0]["symbol"],
     "HGNC_ID": genenames_info["response"]["docs"][0]["hgnc_id"],
     "MANE_Select": genenames_info["response"]["docs"][0].get("mane_select", "N/A")
    }
    return extracted_dict

refseq_transcript_id = "N/A"
ensembl_transcript_id = "N/A"


for transcript in gene_info_output.get("MANE_Select", []):
    if transcript.startswith("NM_"):
        refseq_transcript_id = transcript
    elif transcript.startswith("ENST"):
        ensembl_transcript_id = transcript
    elif 


if refseq_transcript_id == "N/A":
    logger.warning(
        "No MANE Select RefSeq transcript found for gene symbol: %s",
        gene_symbol,
    )

if ensembl_transcript_id == "N/A":
    logger.warning(
        "No MANE Select Ensembl transcript found for gene symbol: %s",
        gene_symbol,
    )

    return gene_info_output, refseq_transcript_id, ensembl_transcript_id #refseq id shd be in genenames
#gene_symbol = input("Enter the gene symbol:")
#reference_source = input("Enter either R for Refseq or E for Ensembl:")
#output_dict = fetch_gene_info(gene_symbol)


#if reference_source.upper() == "R":
   # from refseq_requests import fetch_refseq_transcript
   # transcript_id = output_dict["MANE_Select"]
   # transcript_info = fetch_refseq_trans


#print(output_dict)


import logging
import requests

logger = logging.getLogger(__name__)

URL = "https://rest.genenames.org/"


def fetch_gene_info(gene_symbol):
    path = f"fetch/symbol/{gene_symbol}"

    response = requests.get(
        URL + path,
        headers={"Accept": "application/json"},
    )
    response.raise_for_status()

    gene_info = response.json()
    doc = gene_info["response"]["docs"][0]

    return {
        "up_to_date_symbol": doc["symbol"],
        "HGNC_ID": doc["hgnc_id"],
        "MANE_Select": doc.get("mane_select", []),
    }


def get_mane_transcripts(gene_symbol):
    gene_info_output = fetch_gene_info(gene_symbol)

    refseq_transcript_id = None
    ensembl_transcript_id = None

    for transcript in gene_info_output.get("MANE_Select", []):
        if transcript.startswith("NM_"):
            refseq_transcript_id = transcript
        elif transcript.startswith("ENST"):
            ensembl_transcript_id = transcript

    if not refseq_transcript_id:
        logger.warning(
            "No MANE Select RefSeq transcript found for gene symbol: %s",
            gene_symbol,
        )

    if not ensembl_transcript_id:
        logger.warning(
            "No MANE Select Ensembl transcript found for gene symbol: %s",
            gene_symbol,
        )

    return (
        gene_info_output,
        refseq_transcript_id,
        ensembl_transcript_id,
    )