from wordle_mhs2229 import wordle_mhs2229

import pytest
from wordle_mhs2229 import (
    validate_guess,
    check_guess,
    is_valid_word
)

@pytest.fixture
def common_word_list():
    return [
        "crane", "apple", "hello", "world", "python", 
        "house", "water", "light", "music", "dream",
        "happy", "smile", "peace", "heart", "brain",
        "table", "chair", "phone", "paper", "green"
    ]


# =============================================================================
# PART 1: BASIC TESTING
# =============================================================================

def test_validate_guess():
    """
    Test the validate_guess function with various inputs.
    """

    assert validate_guess("apple") == True      # Valid inputs (correct length, lowercase, alphabetic)

    assert validate_guess("cranes") == False    # Invalid inputs: wrong length
    assert validate_guess("AppLE") == False     # Invalid inputs: uppercase letters
    assert validate_guess('---..') == False     # Invalid inputs: non-alphabetic

    assert validate_guess("")   == False        # Edge cases: empty string
    assert validate_guess(None) == False        # Edge cases: None value
    assert validate_guess(12345) == False       # Edge cases: non-string input

def test_check_guess_basic():
    """
    Test basic check_guess functionality
    """
    all_match_result = [('c', 'green'), ('r', 'green'), ('a', 'green'), ('n', 'green'), ('e', 'green')]
    assert check_guess("crane", "crane") == all_match_result    # All letters match

    no_match_result = [('c', 'gray'), ('l', 'gray'), ('o', 'gray'), ('c', 'gray'), ('k', 'gray')]
    assert check_guess("brain", "clock") == no_match_result     # No letters match

    mix_result = [('c', 'green'), ('h', 'gray'), ('a', 'green'), ('i', 'gray'), ('r', 'yellow')]
    assert check_guess("crane", "chair") == mix_result          # Mixed matches
    

    assert check_guess("crane", "crrane") == []

def test_is_valid_word(common_word_list):
    """
    Test the is_valid_word function.
    """
    assert is_valid_word("apple", common_word_list) == True    # Valid words
    assert is_valid_word("CRANE", common_word_list) == True    # Valid Words

    assert is_valid_word("crate", common_word_list) == False   # Invalid words

    assert is_valid_word("", common_word_list) == False        # Edge cases: empty string
    assert is_valid_word("crane", []) == False          # Edge cases: empty word list
    
# =============================================================================
# PART 2: ADVANCED TESTING
# =============================================================================

@pytest.mark.parametrize("secret_word, guess, expected", [
    ("crane", "crane", [('c', 'green'), ('r', 'green'), ('a', 'green'), ('n', 'green'), ('e', 'green')]),   # Perfect Match
    ("brain", "clock", [('c', 'gray'), ('l', 'gray'), ('o', 'gray'), ('c', 'gray'), ('k', 'gray')]),        # No Match
    ("crane", "chair", [('c', 'green'), ('h', 'gray'), ('a', 'green'), ('i', 'gray'), ('r', 'yellow')]),    # Mixed Results
    ("crane", "creed", [('c', 'green'), ('r', 'green'), ('e', 'yellow'), ('e', 'gray'), ('d', 'gray')]),    # Duplicate Letters in guess
    ("apple", "piper", [('p', 'yellow'), ('i', 'gray'), ('p', 'green'), ('e', 'yellow'), ('r', 'gray')]),   # Additional scenarios of your choice
])
def test_check_guess_comprehensive(secret_word, guess, expected):
    """
    Test check_guess with multiple scenarios using parametrize.
    """
    assert check_guess(secret_word, guess) == expected

def test_word_list_fixture(common_word_list):
    """
    Test the common_word_list fixture to ensure it provides the correct list of words.
    """
    WORD_LIST = [
        "crane", "apple", "hello", "world", "python",
        "house", "water", "light", "music", "dream",
        "happy", "smile", "peace", "heart", "brain",
        "table", "chair", "phone", "paper", "green"
    ]
    assert common_word_list == WORD_LIST




