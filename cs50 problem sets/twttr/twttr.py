def shorten(text):
    vowels = "AEIOUaeiou"
    result = ""

    for char in text:
        if char not in vowels:
            result += char

    return result

def main():
    input_text = input("Input: ")
    output_text = shorten(input_text)
    print(f'Output: {output_text}')

if __name__ == "__main__":
    main()
