import sys


def main(args):
    """
    fonction qui converti des chiffres, lettres
    ou espaces données en argument en morse.
    """
    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ",
                    "B": "-... ",
                    "C": "-.-. ",
                    "D": "-.. ",
                    "E": ". ",
                    "F": "..-. ",
                    "G": "--. ",
                    "H": ".... ",
                    "I": ".. ",
                    "J": ".--- ",
                    "K": "-.- ",
                    "L": ".-.. ",
                    "M": "-- ",
                    "N": "-. ",
                    "O": "--- ",
                    "P": ".--. ",
                    "Q": "--.- ",
                    "R": ".-. ",
                    "S": "... ",
                    "T": "- ",
                    "U": "..- ",
                    "V": "...- ",
                    "W": ".-- ",
                    "X": "-..- ",
                    "Y": "-.-- ",
                    "Z": "--.. ",
                    "0": "----- ",
                    "1": ".---- ",
                    "2": "..--- ",
                    "3": "...-- ",
                    "4": "....- ",
                    "5": "..... ",
                    "6": "-.... ",
                    "7": "--... ",
                    "8": "---.. ",
                    "9": "----. ",
                    }
    if len(args) != 2:
        raise AssertionError("AssertionError: the arguments are bad")
    S = ""
    for char in args[1]:
        if char.isdigit() or char.isalpha():
            if char.islower():
                char = char.upper()
            S += NESTED_MORSE.get(char)
        else:
            raise AssertionError("AssertionError: the arguments are bad")
    print(S)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as e:
        print(e)
