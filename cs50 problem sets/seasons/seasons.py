from datetime import date, datetime
import inflect
import sys

def main():
    dob = input("Date of Birth (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
        if birth_date > date.today():
            raise ValueError("Date of birth cannot be in the future.")
    except ValueError as e:
        sys.exit(e)

    minutes = calculate_minutes_since_birth(birth_date)
    minutes_in_words = convert_number_to_words(minutes)

    print(f"{minutes_in_words.capitalize()} minutes")

def calculate_minutes_since_birth(birth_date):
    today = date.today()
    delta = today - birth_date
    return delta.days * 24 * 60

def convert_number_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number, andword="")

if __name__ == "__main__":
    main()
