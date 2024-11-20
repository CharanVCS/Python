import pytest
from um import count

def test_single_um():
    assert count("hello, um, world") == 1

def test_multiple_ums():
    assert count("um, um, um, um") == 4

def test_um_in_words():
    assert count("yummy um umbrella um") == 2

def test_case_insensitive_um():
    assert count("Um um UM uM") == 4

def test_no_um():
    assert count("hello, world") == 0

def test_um_with_punctuation():
    assert count("um... what's that?") == 1
    assert count("Um, I'm not sure.") == 1

if __name__ == "__main__":
    pytest.main()
