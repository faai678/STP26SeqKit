import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)



# if seq_input is the sequence
def str_to_seq10(seq_input: str) -> str:
    logger.info("Converting sequence to 10-nucleotide format...")
    lower_seq_input = seq_input.lower()
    seq_10 = " ".join(lower_seq_input[i:i+10]for i in range(0, len(lower_seq_input), 10))
    logger.debug(f"Converted sequence: {seq_10}")
    return seq_10



def seq10_to_genb(seq10_input: str) -> str:
    logger.info("Converting sequence to GenBank format...")
    genb_seq = "\n".join(seq10_input[i:i+66]for i in range(0, len(seq10_input), 66))
    logger.debug(f"Converted GenBank sequence: \n{genb_seq}")
    return genb_seq




seq_input = input("Insert gene sequence: ")
seq10_result = str_to_seq10(seq_input)
print(seq10_result)

genb_result = seq10_to_genb(seq10_result)
print(genb_result)


