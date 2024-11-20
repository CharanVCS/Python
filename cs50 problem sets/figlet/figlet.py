import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        font = sys.argv[2]
        if font not in figlet.getFonts():
            sys.exit("Error: Font not found.")
    else:
        sys.exit("Usage: figlet.py [ -f | --font <font_name> ]")
        
    figlet.setFont(font=font)
    text = input("Input: ")
    print(f"Output:{figlet.renderText(text)}")

if __name__ == "__main__":
    main()
