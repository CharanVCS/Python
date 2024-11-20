import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Validate file extensions
    valid_extensions = [".jpg", ".jpeg", ".png"]
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid Input.")

    if input_ext != output_ext:
        sys.exit("Input and output have different extension.")

    try:
        photo = Image.open(input_file)
    except FileNotFoundError:
        sys.exit(f"Error: File '{input_file}' not found")
    except Exception as e:
        sys.exit(f"Error opening '{input_file}': {e}")

    # Open the shirt image
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Error: shirt.png file not found")
    except Exception as e:
        sys.exit(f"Error opening 'shirt.png': {e}")

    # Resize and crop the input image to the size of the shirt image
    muppet = ImageOps.fit(photo, shirt.size)

    # Overlay the shirt image on the input image
    muppet.paste(shirt, shirt)

    try:
        muppet.save(output_file)
    except Exception as e:
        sys.exit(f"Error saving '{output_file}': {e}")


if __name__ == "__main__":
    main()
