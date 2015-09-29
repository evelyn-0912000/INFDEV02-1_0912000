import sys
import re

# Exercise 1: Reverse

text = raw_input("Put in the string you wish to reverse.\n> ")

i = len(text)
while i > 0:
    sys.stdout.write(text[i-1])
    i -= 1

sys.stdout.write('\n')


# Exercise 2: Passwords

password = raw_input("Put in the password whose strength you wish to test.\n> ")

strength = 95 ** len(password) # The amount of printable characters in ASCII is 95; therefore for every extra character there are 95 possibilities.

if len(str(strength)) < 5:
    print("Your password is weak.")
elif len(str(strength)) < 25:
    print("Your password is so-so.")
else:
    print("Your password is strong.")

# Exercise 3: Cryptography

original = raw_input("Put in the string you wish to encode via ROT3.\n> ")
original = original.upper()

if re.sub(r'[A-Z ]', '', original) == '':
    i = 0
    encoded = ""

    while i < len(original):
        ascii = ord(original[i])

        if ord(original[i]) == 32:
            encoded = encoded + ' '
        elif ord(original[i]) > 87:
            encoded = encoded + chr(65 + 3 - (91 - ascii))
        else:
            encoded = encoded + chr(ascii + 3)

        i += 1

    print("The encoded string is \"%s\"." % encoded)
else:
    print("Your string may not have any characters outside of the alphabet and space.")