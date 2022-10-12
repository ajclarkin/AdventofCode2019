# October 2022
# Part 2 - what's the longest path?


from mod_intcode import Intcode


moves = [1, 2, 3, 4]


reverse = {0:0, 1: 2, 2: 1, 3: 4, 4: 3}
paths = []

intcode = Intcode()
locationtype = 0

# Let's make a map
x, y = 0, 0
dx = {1: 0, 2: 0, 3: -1, 4: 1}
dy = {1: -1, 2: 1, 3: 0, 4: 0}
map = dict()


# COMMANDS & RESPONSES
# Only four movement commands are understood: north (1), south (2), west (3), and east (4).
# Responses: 0 - wall / 1 - moved 1 step in that direction / 2 - moved 1 step and found destination




def PrintGrid(map):
    x_min, x_max = 0, 0
    y_min, y_max = 0, 0

    for x, y in map.keys():
        if x < x_min: x_min = x
        if x > x_max: x_max = x
        if y < y_min: y_min = y
        if y > y_max: y_max = y

    # Create lists for each of these - they need to start at 0 so correct for this
    x_offset = 0 - x_min
    y_offset = 0 - y_min
    x_range = x_max - x_min
    y_range = y_max - y_min

    # Initialised rows with dots
    gridlist = [['o' for _ in range(x_range +1)] for _ in range(y_range +1)]

    for x, y in map:
        if map[(x, y)] == 0: gridlist[y + y_offset][x + x_offset] = '#'
        if map[(x, y)] == 1: gridlist[y + y_offset][x + x_offset] = '.'
        if map[(x, y)] == 2: gridlist[y + y_offset][x + x_offset] = '2'

    gridlist[y_offset][x_offset] = '@'

    print(f'X: {x_min} to {x_max}\nY: {y_min} to {y_max}')

    print('\n'.join(''.join(row) for row in gridlist))
    print('\nPath represented by . and unexplored squares by o. Origin is @')





# For the first move there is no previous move to reverse and nothing in the paths list
# so first move is outside the main loop to get these populated.

options = moves.copy()
valid = []
for poss in options:
        locationtype = intcode.RunIntcode(poss)
        if locationtype == 1:
            intcode.RunIntcode(reverse[poss])
            valid.append(poss)

        map[(x + dx[poss], y + dy[poss])] = locationtype

paths.append(valid)



history = dict()
while len(paths) > 0:
    # Get the oldest path and follow all it's moves
    path = paths.pop(0)
    path_length = len(path)

    level = 0
    new_val = 0
    for p in path:
        intcode.RunIntcode(p)
        x = x + dx[p]
        y = y + dy[p]
        level += 1
        if (x,y) not in history:
            history[(x,y)] = level
            new_val += 1


    # Now find what moves are possible from the last square reached in the path
    gen = (i for i in moves if i != reverse[p])
    options = list(gen)     # need this listcomp aboves returns a generator


    valid = []
    for poss in options:
        locationtype = intcode.RunIntcode(poss)

        if locationtype != 0:
            intcode.RunIntcode(reverse[poss])

            valid.append(poss)

        map[(x + dx[poss], y + dy[poss])] = locationtype
        # print(f'[({x + dx[poss]}, {y + dy[poss]})')

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
print(f'Moves made: {path_length}')
print(f'Highest level of unique location: {max( history.values())}')
print(f'New locations added on this path: {new_val}')

# PrintGrid(map)

# 412 is too high
