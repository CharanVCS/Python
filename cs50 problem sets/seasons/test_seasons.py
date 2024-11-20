from seasons import calculate_minutes_since_birth, convert_number_to_words
from datetime import date

def test_calculate_minutes_since_birth():
    assert calculate_minutes_since_birth(date(2023, 1, 1)) == (date.today() - date(2023, 1, 1)).days * 24 * 60
    assert calculate_minutes_since_birth(date(2000, 2, 29)) == (date.today() - date(2000, 2, 29)).days * 24 * 60

def test_convert_number_to_words():
    assert convert_number_to_words(525600) == "five hundred twenty-five thousand six hundred"
    assert convert_number_to_words(1440) == "one thousand four hundred forty"

