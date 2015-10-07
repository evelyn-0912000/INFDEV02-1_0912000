import sys
import math

#def dimensions(shapeName, dim):
#    try:
#        length

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

print(shape)


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

print(shape)

# Full rectangle triangle

shape = ""
row = column = 0

for row in range(0, dim):
    for column in range(0, row+1):
        shape = shape + '*'
    shape = shape + '\n'

print(shape)

# Full isolesces triangle

try:
    length = int(raw_input("What length do you want your triangle to be?\n> "))
    width = int(raw_input("What width do you want your triangle to be?\n> "))
    #length = width = dim
except ValueError:
    print("You need to put in an integer.")
    sys.exit("Error occured, program aborted.")

shape = ""
row = column = 0.0

halfWidth = (float(width) / 2) -.5

for row in range(0, length):
    for column in range(0, width):
        if length % 2 == 1 and column == halfWidth:
            shape = shape + '*'
        elif length % 2 == 0 and (column == math.floor(halfWidth) or column == math.ceil(halfWidth)):
            shape = shape + '*'
        elif column < halfWidth and 1 - (float(row) / length) < (float(column) / halfWidth + 1/halfWidth):
            shape = shape + '*'
        elif column > halfWidth and (float(row) / length ) > (float(column - halfWidth) / halfWidth - 1/halfWidth):
            shape = shape + '*'
        else:
            shape = shape + ' '

        column += 1
    shape = shape + '\n'
    row += 1

print(shape)


# Circle

shape = ""
row = column = 0

radius = float(dim-1)/2 # is also x and y coordinate of middle

for row in range(0, dim):
    for column in range(0, dim):
        hypothenuse = math.sqrt((math.fabs(radius - float(row))) ** 2 + (math.fabs(radius - float(column))) ** 2)
        
        if math.fabs(radius - hypothenuse) < 0.45:
            shape = shape + '*'
        elif math.fabs(-(row-radius*1.6) - (math.floor((column - radius))**2 * .2)) < .8: # y = x^2 * .2
        # -(row-radius*1.6) == (column - radius)**2 * .2...
            if (column > dim * .3 and column < dim * .7) and (row > radius * 1.2 and row < radius * 2):
            # ...within domain <dim * .3, dim * .7> and reach <radius*1.2, radius*2:
                shape = shape + '*'
            else:
                shape = shape + ' '
        else:
            shape = shape + ' '
    shape = shape + '\n'

print(shape)


# ☺

shape = ""
row = column = 0

radius = float(dim-1)/2 # is also x and y coordinate of middle

smile = {
    'x': radius,
    'y': radius + dim * .3
}
