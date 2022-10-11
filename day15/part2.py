# October 2022
# Part 2 - what's the longest path?


from mod_intcode import Intcode


moves = [1, 2, 3, 4]
paths = []

intcode = Intcode()
locationtype = 0


# COMMANDS & RESPONSES
# Only four movement commands are understood: north (1), south (2), west (3), and east (4).
# Responses: 0 - wall / 1 - moved 1 step in that direction / 2 - moved 1 step and found destination




# For the first move there is no previous move to reverse and nothing in the paths list
# so first move is outside the main loop to get these populated.

options = moves.copy()
valid = []
for poss in options:
        locationtype = intcode.RunIntcode(poss)
        if locationtype == 1:
            intcode.RunIntcode(reverse[poss])
            valid.append(poss)

paths.append(valid)



valid = [1]     # for the purposes of the while loop
while len(valid) > 0:
    # Get the oldest path and follow all it's moves
    path = paths.pop(0)

    for p in path:
        intcode.RunIntcode(p)


    # Now find what moves are possible from the last square reached in the path
    gen = (i for i in moves if i != reverse[p])
    options = list(gen)     # need this listcomp aboves returns a generator


    valid = []
    for poss in options:
        locationtype = intcode.RunIntcode(poss)

        if locationtype != 0:
            intcode.RunIntcode(reverse[poss])
            valid.append(poss)

    # valid now contains all the possible moves.
    # Each one of these should be appended to the original path and stuck on the end of paths as a viable path

    reverse_path = path.copy()

    for v in valid:
        new_path = path.copy()
        new_path.append(v)
        paths.append(new_path)


    reverse_path.reverse()
    for p in reverse_path:
        intcode.RunIntcode(reverse[p])
        x = x + dx[reverse[p]]
        y = y + dy[reverse[p]]





print(f'Reached the limit of the area.')
print(f'Moves made: {len(paths[-1])}')

