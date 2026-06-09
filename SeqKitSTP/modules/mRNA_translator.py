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