#!/usr/bin/env python
"""
een script waarbij je om input vraagt achter een willekeurig woord en
waarbij het script het woord achterstevoren weergeeft.
"""

# Import


__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


def main():
    word = input("Give me a word to put backwards.\n")
    print(word[::-1])


if __name__ == '__main__':  # code to execute if called from command-line
    main()
