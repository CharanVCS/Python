from plates import is_valid

def test_valid_plates():
    assert is_valid("AB123") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("AB12") == True

def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_invalid_start():
    assert is_valid("1ABC") == False
    assert is_valid("A1BC") == False
    assert is_valid("1234") == False

def test_invalid_characters():
    assert is_valid("ABC@123") == False
    assert is_valid("AB#CDE") == False
    assert is_valid("A#BCDE") == False

def test_invalid_number_sequence():
    assert is_valid("AB012") == False
    assert is_valid("A12B3") == False
    assert is_valid("AB12C3") == False
