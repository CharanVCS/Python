from twttr import shorten

def test_str():
    assert shorten("Hi iam string")=="H m strng"

def test_mixed_characters():
    assert shorten("12345") == "12345"
    assert shorten("hello123") == "hll123"
    assert shorten("h3ll0") == "h3ll0"
    assert shorten("!@#$$%") == "!@#$$%"

def test_spaces():
    assert shorten("hello world") == "hll wrld"
    assert shorten("AEIOU aeioU") == " "
