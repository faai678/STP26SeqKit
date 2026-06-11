from SeqKitSTP.modules import sequence_processing
import pytest

#test for clean_sequence()
def test_clean_sequence_removes_whitespace():
    input_seq = " A T G C \n T A C G "
    expected_output = "ATGCTACG"
    assert sequence_processing.clean_sequence(input_seq) == expected_output

def test_clean_sequence_empty_string():
    assert sequence_processing.clean_sequence("") == "" 

def test_clean_sequence_no_whitespace():
    input_seq = "ATGCTACG"
    expected_output = "ATGCTACG"
    assert sequence_processing.clean_sequence(input_seq) == expected_output 

#test for validate_sequence()
def test_validate_sequence_valid_dna():
    valid_bases = "ATGC"
    sequence = "ATGCTAGC"
    # Should not raise an error for valid DNA sequence.
    try:
        sequence_processing.validate_sequence(sequence, valid_bases, "DNA")
    except SequenceError:
        pytest.fail("validate_sequence() raised SequenceError unexpectedly!")

def test_validate_sequence_invalid_dna():
    valid_bases = "ATGC"
    sequence = "ATGCTXAGC"
    # Should raise SequenceError for invalid DNA sequence.
    with pytest.raises(SequenceError):
        sequence_processing.validate_sequence(sequence, valid_bases, "DNA")

def test_validate_sequence_empty_string():
    valid_bases = "ATGC"
    sequence = ""
    # Should raise ValueError for empty sequence.
    with pytest.raises(ValueError):
        sequence_processing.validate_sequence(sequence, valid_bases, "DNA")

def test_validate_sequence_non_string_input():
    valid_bases = "ATGC"
    sequence = 12345  # Not a string
    # Should raise TypeError for non-string input.
    with pytest.raises(TypeError):
        sequence_processing.validate_sequence(sequence, valid_bases, "DNA") 


