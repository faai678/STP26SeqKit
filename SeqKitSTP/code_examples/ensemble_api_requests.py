"""
Retrieving Ensemble transcript using API endpoints.

"""
import logging
logger = logging.getLogger(__name__)
import requests
import json
import subprocess

def fetch_ensembl_transcript(gene_id):
    """
    Retrieve a transcript record from Ensembl.

    Parameters
    ----------
    transcript_id : str
        An Ensembl transcript accession including its version number.

        Examples:
            ENST00000371817.8
    
    1. Fetch metadata using lookup/id
    2. fetch sequence using sequence/id
    3. convert json into python dict

    Returns
    -------
    dict
        The Ensembl record represented as a Python dictionary.
    Return format:
            {

            "id": <transcript accession and version>,

            "name": <transcript name information>,

            "status": <Mane Select or other e.g. MANE Plus Clinical, RefSeq Select, Ensembl canonical or other>

            "sequence": <cDNA sequence>,

            "cds_start": <integer>,

            "cds_end": <integer>

            }

    """
    logger.info("Fetching Ensembl transcripst for: %s", gene_id)
    
    base_url = "http://rest.ensembl.org/"
    headers_json = {"Content-Type": "application/json"}

    # fetch metadata 
    lookup_url = base_url + "lookup/id/" + gene_id
    lookup_params = {
        "expand": 1,
        "mane": 1}
    meta_data_response = requests.get(lookup_url, headers=headers_json, params=lookup_params)
    
    try:
        meta_data_response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logger.error("HTTP error occurred: %s", e)
        return {"HTTPerror": str(e)}


    # fetch json data from responses
    meta_data = meta_data_response.json()



        
    # okay this code works
    for transcript in meta_data["Transcript"]:

        mane = transcript.get("MANE", [])

        # Skip if no MANE and not canonical
        if not mane and transcript.get("is_canonical") != 1:
            continue

        if any(m.get("type") == "MANE_Select" for m in mane):
            status = "MANE Select"

        elif any(m.get("type") == "MANE_Plus_Clinical" for m in mane):
            status = "MANE Plus Clinical"

        elif transcript.get("is_canonical") == 1:
            status = "Ensembl canonical"

        else:
            status = "Unknown"

        final_status = print(transcript["id"], status)
        cds_start = transcript.get("start", None)
        cds_end = transcript.get("end", None)
    


    # fetch cdna sequence
    sequence_url = base_url + "sequence/id/" + meta_data.get("canonical_transcript", [None])[0:15]
    sequence_params_cdna = {"type": "cdna"}
    sequence_response_cdna = requests.get(sequence_url, headers=headers_json, params=sequence_params_cdna)

    # check if request is successful
    try:
        sequence_response_cdna.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logger.error("HTTP error occurred: %s", e)
        return {"HTTPerror": str(e)}

    # fetch cds sequence
    sequence_url = base_url + "sequence/id/" + meta_data.get("canonical_transcript", [None])[0:15]
    sequence_params_cds = {"type": "cds"}
    sequence_response_cds = requests.get(sequence_url, headers=headers_json, params=sequence_params_cds)

    # check if request is successful    
    try:
        sequence_response_cds.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logger.error("HTTP error occurred: %s", e)
        return {"HTTPerror": str(e)}

    sequence_data_cdna = sequence_response_cdna.json()
    sequence_data_cds = sequence_response_cds.json()
        # okay so canonical txcpt wd usually be the mane, if cannical txpt = trancript id in ismanestatus, then true. then use the id to put into sequence/id to get both cdna and cds sequence.
        #Construct dictionary
    extracted_dict = {
                "id" : f"{meta_data.get("canonical_transcript")}",
                "name" : meta_data.get('display_name', 'Unknown'),
                "status" : final_status,
                "sequence" : sequence_data_cdna.get('seq'),
                "cds_start" : cds_start,
                "cds_end" : cds_end
                }
    return extracted_dict




output_data = fetch_ensembl_transcript(input("Enter Gene ID: "))

dict_string = json.dumps(output_data, indent=4)
# 2. Pipe the string into a new VS Code window
process = subprocess.Popen(["code", "-"], stdin=subprocess.PIPE, text=True)
process.communicate(input=dict_string)