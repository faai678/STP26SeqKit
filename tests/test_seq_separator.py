import pytest  # pytest test framework
from SeqKitSTP.modules import seq_separator
  # module under test


# ------------------------------
# Tests for block_sequence()
# ------------------------------

def test_block_sequence_regular_case():
    # Typical DNA sequence input.
    seq = "aggagtaagcccttgcaactggaaatacacccattg"

    # Expect fixed-width chunks of 5 bases.
    # Final chunk may be shorter if sequence length is not divisible by 5.
    expected = [
        'aggag', 'taagc', 'ccttg', 'caact',
        'ggaaa', 'tacac', 'ccatt', 'g'
    ]

    # Verify normal chunking behaviour.
    assert seq_separator.block_sequence(seq, 5) == expected

def test_block_sequence_block_size_as_string():
    # chunk_by must be an integer.
    seq = "aggagtaagcccttgcaactggaaatacacccattg"

    # A string should fail because slicing expects an integer index.
    with pytest.raises(TypeError):
        seq_separator.block_sequence(seq, "5")


def test_block_sequence_empty_sequence():
    # Empty input should return an empty list rather than fail.
    assert seq_separator.block_sequence("", 5) == []


def test_block_sequence_chunk_larger_than_sequence():
    # If chunk size exceeds sequence length,
    # the whole sequence should be returned as one chunk.
    assert seq_separator.block_sequence("agg", 10) == ["agg"]