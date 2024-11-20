import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) >2 :
        print("Too many command-line arguments")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        print("Not a Python file.")
        sys.exit(1)

    if not os.path.isfile(filename):
        print("file does not exist.")
        sys.exit(1)

    try:
        loc = count_lines_of_code(filename)
        print(f"{loc}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def count_lines_of_code(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line and not stripped_line.startswith('#'):
                count += 1
    return count

if __name__ == "__main__":
    main()
