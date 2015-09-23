﻿import re
import random
import sys

def runChoice(correction):
    running = raw_input(correction + "\nEnter 'y' to restart the section, 'a' to abort, and anything else to continue on.\n> ")
    if running == 'y':
        return True
    elif running == 'a':
        sys.exit("User chose to abort during the runChoice sequence.")
    return False

running = True
skip = raw_input("Do you wish to skip the next part of the program? ('y' for yes, anything else to continue per usual.)\n> ")

while running == True and skip != 'y':
    try:
        fahrenheit = float(raw_input("What is the temperature in Fahrenheit you wish to convert to Celsius?\n> "))

        if fahrenheit < -456.670 or fahrenheit > 2.54 * 1000000000000000000000000000000000:     #2.54e32
            running = runChoice("The temperature needs to be between absolute zero and the Planck temperature.")
            continue

        celsius = (fahrenheit - 32) / 1.8

        print("The temperature in Celsius is " + str(celsius) + '.')
        
        celsius = float(raw_input("What is the temperature in Celsius you wish to convert to Kelvin?\n> "))
        
        if celsius < -273.15 or celsius > 1.41 * 1000000000000000000000000000000000: # 1.41e32
            running = runChoice("The temperature needs to be between absolute zero and the Planck temperature.")
            continue
        
        kelvin = celsius - 273.15
        
        print("The temperature in Kelvin is " + str(kelvin) + '.')

        number = float(raw_input("What is the number you wish to have the absolute value of?\n> "))
        decimals = number - int(number)
        
        if decimals > 0:
            number = int(number)
    
        if number < 0:
            number = -number

        print("The absolute value of your number is " + str(number) + '.')
        
        running = False

    except ValueError:
        running = runChoice("Invalid number: Either floating point or integer should work.")
        continue

skip = raw_input("Do you wish to skip the next part of the program? ('y' for yes, anything else to continue per usual.)\n> ")

gestures = ["rock", "scissors", "paper", "lizard", "Spock"]

gestureTuples = {
    "rock": {"lizard": "crushes", "scissors": "crushes"},
    "scissors": {"paper": "cut", "lizard": "decapitates"},
    "paper": {"rock": "covers", "Spock": "disproves"},
    "lizard": {"paper": "eats", "Spock": "poisons"},
    "Spock": {"scissors": "smashes", "rock": "vaporizes"}
}

while running == True and skip != 'y':
    playerChoice = raw_input("Rock, paper, scissors, lizard, or Spock?\n> ")
    playerChoice = re.sub("[^a-zA-Z]", "", str.lower(playerChoice))
    
    if playerChoice == "spock":
        playerChoice = "Spock"

    gestureOk = False

    for gesture in gestureTuples:
        if playerChoice == gesture:
            gestureOk = True
            break
    
    if gestureOk:
        CPUChoice = gestures[random.randint(1, 5) - 1]

        if CPUChoice in gestureTuples[playerChoice]:
            print "%s %s %s. You win!" % (str.title(playerChoice), gestureTuples[playerChoice][CPUChoice], CPUChoice)
            runChoice("Play again?")
        elif playerChoice in gestureTuples[CPUChoice]:
            print "%s %s %s. You lose!" % (str.title(CPUChoice), gestureTuples[CPUChoice][playerChoice], playerChoice)
            runChoice("Play again?")
        else:
            print "%s and %s don't interact. It's a draw." % (str.title(playerChoice), CPUChoice)
            runChoice("Play again?")
    else:
        runChoice("\"%s\" is not a valid choice." % playerChoice)
    