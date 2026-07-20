import requests
import json

gene_id = input("Enter the gene ID: ")  

r = requests.get(
    f"https://rest.ensembl.org/lookup/id/{gene_id}",
    headers={"Accept": "application/json"},
    params={"expand": 1, "mane": 1}
)

r.raise_for_status()

data = r.json()

for transcript in data["Transcript"]:
    mane = transcript.get("MANE", [])
    if mane:
        print(f"\n{transcript['id']}")
        print(json.dumps(transcript["MANE"], indent=4))
'''
for transcript in data["Transcript"]:

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

    print(transcript["id"], status)

# so this code works to get the mane select but need to put gene id. but how to get trasncript??
# brca2 gene ENSG00000139618
# ENSG00000132155 raf1
# ENSG00000157764 braf

#to get start and end from sequence. we want from the cds not the genomic coordinates. so frist is get the cdna seq and then the 
'''