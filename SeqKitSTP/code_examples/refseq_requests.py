"""
Example: Retrieving a RefSeq transcript from the NCBI GenBank database.

This example introduces the Python Requests library by making a simple
HTTP GET request to the NCBI Entrez API.

Learning objectives
-------------------
After completing this example you should understand:

1. What an API endpoint is.
2. What query parameters are.
3. How the Requests library builds a URL automatically.
4. How to retrieve data from a web server.
5. How to convert XML into a Python dictionary.
"""

import requests
import xmltodict


def fetch_genbank_transcript(transcript_id):
    """
    Retrieve a transcript record from GenBank.

    Parameters
    ----------
    transcript_id : str
        A RefSeq transcript accession including its version number.

        Examples:
            NM_000093.5
            NM_004006.3

    Returns
    -------
    dict
        The GenBank record represented as a Python dictionary.
    """

    # ------------------------------------------------------------------
    # Step 1 - Define the API endpoint.
    #
    # An endpoint is simply the web address of an API service.
    #
    # In this case we are using NCBI's "EFetch" service, which allows
    # us to retrieve records from one of the NCBI databases.
    #
    # Notice that there is no transcript accession in the URL.
    # We supply that separately using query parameters.
    # ------------------------------------------------------------------

    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    # ------------------------------------------------------------------
    # Step 2 - Define the query parameters.
    #
    # Many web APIs expect extra information to be supplied after the URL.
    #
    # This extra information is called the "query string".
    #
    # A query string begins with a '?'
    #
    # Example:
    #
    # https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=NM_000093.5&retmode=xml
    #
    # It consists of one or more key=value pairs separated by '&'.
    #
    # Instead of constructing this text ourselves, we create a normal
    # Python dictionary.
    #
    # Requests automatically converts:
    #
    # {
    #     "db": "nucleotide",
    #     "id": "NM_000093.5",
    #     "retmode": "xml"
    # }
    #
    # into
    #
    # ?db=nucleotide&id=NM_000093.5&retmode=xml
    #
    # and appends it to the URL before contacting the server.
    #
    # This is one of the reasons Requests is so convenient.
    # ------------------------------------------------------------------

    params = {
        "db": "nucleotide",      # Search the nucleotide database
        "id": transcript_id,     # The transcript we wish to retrieve
        "retmode": "xml",        # Return the record as XML
    }

    # ------------------------------------------------------------------
    # Step 3 - Send the HTTP request.
    #
    # The Requests library now combines:
    #
    #     url
    #
    # with
    #
    #     params
    #
    # to produce the complete URL:
    #
    # https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi
    #     ?db=nucleotide
    #     &id=NM_000093.5
    #     &retmode=xml
    #
    # It then sends an HTTP GET request to the NCBI server.
    #
    # The returned Response object contains:
    #
    # • the HTTP status code
    # • response headers
    # • the returned data
    # ------------------------------------------------------------------

    response = requests.get(url, params=params)

    # ------------------------------------------------------------------
    # Step 4 - Check whether the request succeeded.
    #
    # Every HTTP response includes a status code.
    #
    # Successful request:
    #
    #     HTTP/1.1 200 OK
    #
    # Resource not found:
    #
    #     HTTP/1.1 404 Not Found
    #
    # Internal server error:
    #
    #     HTTP/1.1 500 Internal Server Error
    #
    # If the server returned "404 Not Found", it may send back a small HTML
    # error page instead of the XML transcript we requested.
    #
    # For example:
    #
    # <html>
    #   <head><title>404 Not Found</title></head>
    #   <body>
    #       <h1>Not Found</h1>
    #       <p>The requested resource could not be found.</p>
    #   </body>
    # </html>
    #
    # If we attempted to parse this as GenBank XML, our program would fail
    # with a confusing error because it is not the data we expected.
    #
    # raise_for_status() checks the HTTP status code and immediately raises
    # an exception if the request failed, preventing us from processing an
    # error page as though it were biological data.
    # ------------------------------------------------------------------

    response.raise_for_status()

    # ------------------------------------------------------------------
    # Step 5 - Read the server response.
    #
    # response.text contains the raw XML document returned by GenBank.
    #
    # XML is difficult to work with directly, so we convert it into a
    # Python dictionary.
    # ------------------------------------------------------------------

    record = xmltodict.parse(response.text)

    # ------------------------------------------------------------------
    # Step 6 - Extract the transcript record.
    #
    # The XML document contains a top-level element called "GBSet".
    #
    # Inside this is one or more "GBSeq" records.
    #
    # Here we simply return the transcript record itself.
    # ------------------------------------------------------------------

    return record["GBSet"]["GBSeq"]


# ----------------------------------------------------------------------
# Example usage
# ----------------------------------------------------------------------

if __name__ == "__main__":

    # Retrieve the COL5A1 RefSeq transcript
    transcript = fetch_genbank_transcript("NM_000093.5")

    print("Accession:")
    print(transcript["GBSeq_accession-version"])

    print()

    print("Definition:")
    print(transcript["GBSeq_definition"])

    print()

    print("First 100 bases:")
    print(transcript["GBSeq_sequence"][:100].upper())