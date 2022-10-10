# October 2022
# This is a fork of part1b and I'm going to try to solve the problem

from turtle import position
from mod_intcode import Intcode



x, y = 0, 0
dx = {1: 0, 2: 0, 3: -1, 4: 1}
dy = {1: -1, 2: 1, 3: 0, 4: 0}
reverse = {0:0, 1: 2, 2: 1, 3: 4, 4: 3}

paths = []

# Only four movement commands are understood: north (1), south (2), west (3), and east (4).
# Responses: 0 - wall / 1 - moved 1 step in that direction / 2 - moved 1 step and found destination




def GetPossibleDirections(prev):
    moves = [1, 2, 3, 4]
    reverse = {0:0, 1: 2, 2: 1, 3: 4, 4: 3}

    gen = (i for i in moves if i != reverse[prev])
    options = list(gen)     # need this listcomp aboves returns a generator

    for poss in options:
        locationtype = intcode.RunIntcode(poss)
        if locationtype == 0:
            options.remove(poss)
        if locationtype == 1:
            intcode.RunIntcode(reverse[poss])
        else:
            ## WHAT TO DO WHEN OXYGEN FOUND
            pass

        



# Initial setup - instantiate the objects
intcode = Intcode()
locationtype = intcode.RunIntcode()

for m in moves:
    locationtype = intcode.RunIntcode(m)

    if locationtype == 0:
        # position not changed
        print(f'Tried {m}, got {locationtype}')
    elif locationtype == 1:
        # position changed
        # record then reverese
        print(f'Tried {m}, got {locationtype}')
        intcode.RunIntcode(reverse[m])
    else:
        # Found the oxygen
        print(f'Found the oxygen supply')


