#!/usr/bin/env python
"""
Info about our project comes here.
"""

# Import


__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


def main():
    list = [['.', '.', '.', '.', '.', '.'],
             ['.', 'O', 'O', '.', '.', '.'],
             ['O', 'O', 'O', 'O', '.', '.'],
             ['O', 'O', 'O', 'O', 'O', '.'],
             ['.', 'O', 'O', 'O', 'O', 'O'],
             ['O', 'O', 'O', 'O', 'O', '.'],
             ['O', 'O', 'O', 'O', '.', '.'],
             ['.', 'O', 'O', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.']]

    a = input("In wich direction do you want to print? Type up or down.\n")

    if a == "down":
        for x in range(6):  # 6 values bij the X-comme
            for y in range(9):  # 9 values bij the Y-comme
                if y < 8:
                    print(list[y][-(x + 1)], end="")  # Print out the matrix but 90 degrees anti-clockwise
                else:
                    print(list[y][x])

    print("\n")

    # Reverse 270 degrees
    if a == "up":
        for x in range(6):  # 6 values bij the X-comme
            for y in range(9):  # 9 values bij the Y-comme
                if y < 8:
                    print(list[y][+(x)], end="")  # Print out the matrix but 90 degrees clockwise
                else:
                    print(list[y][x])

if __name__ == '__main__':  # code to execute if called from command-line
    main()
