# October 2022
# This thing has taunted me for years. I'm doing a re-write.


from mod_intcode import Intcode


moves = [1, 2, 3, 4]
reverse = {0:0, 1: 2, 2: 1, 3: 4, 4: 3}
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


# Now we're going to remove and follow the oldest path from the paths list.
# # Follow it to it's end then at the end test each direction.
# Each valid direction will have a new path saved to the end of the list - the path we followed plus the valid new direction.
# The we'll backtrack all the way to the origin. (Yes - inefficient but I want this solved.)

while locationtype != 2:
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



# For part 2 we need to work out the longest path from the oxygen supply
# Save the path to oxygen, follow it, then run the whole thing again until there are no moves left.

path_o2 = paths[-1].copy()
for p in path_o2:
        intcode.RunIntcode(p)

paths = []

options = moves.copy()
valid = []
for poss in options:
        locationtype = intcode.RunIntcode(poss)
        if locationtype == 1:
            intcode.RunIntcode(reverse[poss])
            valid.append(poss)

paths.append(valid)



while len(paths) > 0:
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

print(f'Reached the limit of the area.')
print(f'Moves made: {len(path)}')

