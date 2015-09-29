import sys
import math

try:
    dim = int(raw_input("What is the length you wish the squares and the full rectangular triangle to have?\n> "))
except ValueError:
    print("You need to put in an integer.")
    sys.exit("Error occured, program aborted.")

# Full square

shape = ""
row = column = 0

for row in range(0, dim):
    for column in range(0, dim):
        shape = shape + '*'
    shape = shape + '\n'

#print(shape)


# Hollow square

shape = ""
row = column = 0

for row in range(0, dim):
    for column in range(0, dim):
        if row == 0 or row == dim-1:
            shape = shape + '*'
        elif column == 0 or column == dim-1:
            shape = shape + '*'
        else:
            shape = shape + ' '
    shape = shape + '\n'

#print(shape)

# Full rectangle triangle

shape = ""
row = column = 0

for row in range(0, dim):
    for column in range(0, row+1):
        shape = shape + '*'
    shape = shape + '\n'

#print(shape)

# Full isolesces triangle

try:
    #length = int(raw_input("What length do you want your triangle to be?\n> "))
    #width = int(raw_input("What width do you want your triangle to be?\n> "))
    length = width = dim
except ValueError:
    print("You need to put in an integer.")
    sys.exit("Error occured, program aborted.")

shape = ""
row = column = 0.0

halfWidth = math.floor(float(width) / 2)

for row in range(0, length):
    for column in range(0, width):
        if column == halfWidth and not (row == 0 and length % 2 == 1):
            shape = shape + '*'
        #elif (column == halfWidth or column == halfWidth+1) and length % 2 == 0:
        #    shape = shape + '*'
        elif 1 - (float(column) / halfWidth) < (float((row)) / length) and not (column > halfWidth):
            shape = shape + '*'
        elif (float(column) - halfWidth) / halfWidth < (float((row)) / length) and not column < halfWidth:
            shape = shape + '*'
        else:
            shape = shape + ' '

        column += 1
    shape = shape + '\n'
    row += 1

#print(shape)


# Circle

shape = ""
row = column = 0

radius = float(dim-1)/2 # is also x and y coordinate of middle

for row in range(0, dim):
    for column in range(0, dim):
        hypothenuse = math.sqrt((math.fabs(radius - float(row))) ** 2 + (math.fabs(radius - float(column))) ** 2)
        
        if math.fabs(radius - hypothenuse) < 0.45:
            shape = shape + '*'
        else:
            shape = shape + ' '
    shape = shape + '\n'

print(shape)