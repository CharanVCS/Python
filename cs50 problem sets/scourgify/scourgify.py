import csv
import sys

def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Ensure the input file exists and is readable
    try:
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            data = [row for row in reader]
    except FileNotFoundError:
        sys.exit(f"Error: File '{input_file}' not found")
    except Exception as e:
        sys.exit(f"Error reading '{input_file}': {e}")

    # Process data and write to the output file
    try:
        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                # Split the name into first and last
                last, first = row['name'].split(', ')
                house = row['house']
                writer.writerow({'first': first, 'last': last, 'house': house})
    except Exception as e:
        sys.exit(f"Error writing to '{output_file}': {e}")

if __name__ == "__main__":
    main()
