#!/usr/bin/env python
"""
Een raadspelletje waarbij je een woord moet raden dat in een lijst staat
De lijst mag je kiezen:
ofwel uit een bestand lezen
ofwel zelf een lijst samenstellen in je script
"""

# Import


__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


def main():
    list = ["appel", "banaan", "kiwi", "mango", "ananas"]
    y = 0
    i = 3
    while y < 3:
        guess = input(f"Guess the word. You can guess {i} more times.\n")
        for x in list:
            if guess == x:
                y+=3
                print("Congratz you won.")
        else:
            y+=1
            i-=1



if __name__ == '__main__':  # code to execute if called from command-line
    main()
