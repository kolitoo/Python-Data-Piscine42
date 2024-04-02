import sys
import string


def main(args):
    """
    This function takes a string and print what kind of characters are in it.
    """
    if len(args) >= 2:
        raise AssertionError("More than 1 arguments.")
    if len(args) == 1:
        text = input("What is the text to count?\n")
    else:
        text = args[1]
    upper_letter = 0
    lower_letter = 0
    ponctuation = 0
    space = 0
    digits = 0
    for i in range(len(text)):
        if text[i].isupper():
            upper_letter += 1
        if text[i].islower():
            lower_letter += 1
        if text[i].isdigit():
            digits += 1
        if text[i] in string.punctuation:
            ponctuation += 1
        if text[i].isspace():
            space += 1

    print(f"The texte contain {len(text)} characters:")
    print(f"{upper_letter} upper letters")
    print(f"{lower_letter} lower letters")
    print(f"{ponctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
