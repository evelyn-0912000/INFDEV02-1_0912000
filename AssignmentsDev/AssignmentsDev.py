import sys
import math

name = raw_input("What is your name?\n> ")
print "Hi " + name + '.'

try:
    length = int(raw_input("How long do you wish your square to be (in asterisks)?\n> "))

    if length > 4:
        for line in range(0, length):
            content = ""
            for column in range(0, length):
                if line == 0:
                    content = content + '*'
                elif length - line - column < (length - line) / 2 + 2 and column < length / 2 + line / 2:
                    content = content + '*'
                elif length - column == 1 or length - line == 1:
                    content = content + '*'
                else:
                    content = content + ' '
            print content

    else:
        print str(length) + " is not a valid number. Try an integer of five or larger."

except ValueError:
    print("That's not a valid number, wrong type. Try again.")