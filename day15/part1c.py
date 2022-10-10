# October 2022
# This is a fork of part1b and I'm going to try to solve the problem

from turtle import position
from mod_intcode import Intcode

x, y = 0, 0
moves = [1, 2, 3, 4]
reverse = {0:0, 1: 2, 2: 1, 3: 4, 4: 3}


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


