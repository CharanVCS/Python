# text to textimgaes
import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    # Check the number of command-line arguments
    if len(sys.argv) == 1:
        # No font specified, use a random font
        font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        # Specific font requested
        font = sys.argv[2]
        if font not in figlet.getFonts():
            sys.exit("Error: Font not found.")
    else:
        sys.exit("Usage: figlet.py [ -f | --font <font_name> ]")

    # Set the font
    figlet.setFont(font=font)

    # Prompt the user for text
    text = input("Input: ")

    # Render and print the text in the desired font
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
