import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        font = random.choice(available_fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:

        font = sys.argv[2]
        if font not in available_fonts:
            sys.exit("Invalid usage")
    else:

        sys.exit("Invalid usage: figlet.py [-f FONT_NAME]")


    figlet.setFont(font=font)

    text = input("Input: ")

    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
