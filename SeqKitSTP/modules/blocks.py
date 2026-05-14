import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)



# if seq_input is the sequence
def str_to_genb():
    logger.info("Converting sequence to GenBank format...")
    lower_seq_input = str(seq_input.lower())
    seq_genbank = str(" ".join(s[i:i+3]for i in range(0, len(s), 10)))
df

    return seq_genbank



seq_input: str.input("Insert gene sequence: ") -> str

blocks_function()



seq_input = "atcgatgctactcgatacgc"
print(" ".join(s[i:i+3]for i in range(0, len(s), 3)))
