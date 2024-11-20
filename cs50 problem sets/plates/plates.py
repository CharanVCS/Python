
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    if not s[:2].isalpha():
        return False
    if not numbers_at_end(s):
        return False
    if contains_invalid_characters(s):
        return False
    return True

def numbers_at_end(s):
    number_found = False
    for i, char in enumerate(s):
        if char.isdigit():
            if char == '0' and (i == 2 or (i > 2 and not s[i-1].isdigit())):
                return False
            number_found = True
        elif number_found:
            return False
    return True

def contains_invalid_characters(s):
    for char in s:
        if not char.isalnum():
            return True
    return False

main()
