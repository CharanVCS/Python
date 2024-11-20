import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(filename) as file:
            reader = csv.reader(file)
            headers = next(reader)
            table = [row for row in reader]
    except FileNotFoundError:
        sys.exit(f"Error: File '{filename}' not found")
    except Exception as e:
        sys.exit(f"Error: {e}")

    print(tabulate(table, headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
