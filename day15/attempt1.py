# This incompletely discovers a path
# It also stops at a certain path length and so that's hard-coded into it

from mod_intcode import Intcode

x, y = 0, 0




class GridMap:

    dx = {1: 0, 2: 0, 3: -1, 4: 1}
    dy = {1: -1, 2: 1, 3: 0, 4: 0}
    reverse = {0:0, 1: 2, 2: 1, 3: 4, 4: 3}

    def __init__(self):
        self.x, self.y = 0, 0
        self.map = dict()
        self.moves = [x for x in range(1,5)]
        self.prev = 0


    def GetPossibleDirections(self):
        # Returns a list of directions to move, excluding previous move
        gen = (i for i in self.moves if i != self.reverse[self.prev])
        options = list(gen)

        for poss in options:
            if self.GetPositionInfo(self.x + self.dx[poss], self.y + self.dy[poss]) == 0:
                options.remove(poss)

        # Append the previous move as the final option - will only be taken if nothing else works
        # Note we reverse it - ig the last move was to move north then moving sound would take us to previous location
        options.append(self.reverse[self.prev])
        return options


    def SavePositionInfo(self, direction, result):
        self.map[(self.x + self.dx[direction], self.y + self.dy[direction])] = result


    def GetPositionInfo(self, x, y):
        # Get the info for any x and y position
        if (x, y) in self.map:
            return self.map[(x, y)]
        else:
            return None


    def Move(self, direction):
        self.x = self.x + self.dx[direction]
        self.y = self.y + self.dy[direction]
        self.prev = direction


    def PrintGrid(self):
        x_min, x_max = 0, 0
        y_min, y_max = 0, 0

        for x, y in self.map.keys():
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

        for x, y in self.map:
            if self.map[(x, y)] == 0: gridlist[y + y_offset][x + x_offset] = '#'
            if self.map[(x, y)] == 1: gridlist[y + y_offset][x + x_offset] = '.'
            if self.map[(x, y)] == 2: gridlist[y + y_offset][x + x_offset] = '2'

        gridlist[y_offset][x_offset] = '@'

        print(f'X: {x_min} to {x_max}\nY: {y_min} to {y_max}')

        print('\n'.join(''.join(row) for row in gridlist))
        print('\nPath represented by . and unexplored squares by o. Origin is @')


# Initial setup - instantiate the objects
intcode = Intcode()
result = intcode.RunIntcode()
grid = GridMap()


while result != '' and result != 2:
    dirs = grid.GetPossibleDirections()

    for d in dirs:
        # print(f'Try direction {d}')
        result = intcode.RunIntcode(d)
        # print(f'Outcome: {result}')
        grid.SavePositionInfo(d, result)

        if result != 0:
            grid.Move(d)

            if result == 2:
                print(f'Found the 2 spot: {grid.x}, {grid.y}')

            break

    # print(grid.map)
    print(f'{grid.x}, {grid.y}\t {len(grid.map)}')

    if len(grid.map) == 206:
        print(grid.map)
        break

print(f'Found the 2 spot: {grid.x}, {grid.y}')
grid.PrintGrid()
