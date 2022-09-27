from mod_intcode import Intcode

x, y = 0, 0




class GridMap:

    dx = {1: 0, 2: 0, 3: -1, 4: 1}
    dy = {1: -1, 2: 1, 3: 0, 4: 0}
    reverse = {0:0, 1: 2, 2: 1, 3: 4, 4: 3}

    def __init__(self):
        self.x, self.y = 0, 0
        self.map = dict()       # save map of walls / open space
        self.history = dict()   # save history of explored territory
        self.adjacent = dict()  # how many adjacent boxes are there
        self.moves = [x for x in range(1,5)]
        self.prev = 0
        self.move_counter = 0


    def GetPossibleDirections(self):
        # Returns a list of directions to move, excluding previous move
        gen = (i for i in self.moves if i != self.reverse[self.prev])
        options = list(gen)

        for poss in options:
            if self.GetPositionInfo(self.x + self.dx[poss], self.y + self.dy[poss]) == 0:
                options.remove(poss)

        # # Append the previous move as the final option - will only be taken if nothing else works
        # # Note we reverse it - ig the last move was to move north then moving sound would take us to previous location
        # options.append(self.reverse[self.prev])
        return options
        

    def MapSurroundingSquares(self):
        '''
            Identify how many adjacent spaces there are (should always by 1+)
            Do this by checking if we know about adjacent boxes already and if not try to move there - and move back if move successful
            self.adjacent keeps a note of how many spaces are adjacent
            Return the number of adjacent squares which are not walls
        '''
        if (self.x, self.y) not in self.adjacent:
            # Except for the first move we know there will always be at least one adjacent square
            if self.prev != 0:
                adj = 1
            else:
                adj = 0

            dirs = self.GetPossibleDirections()
            for d in dirs:
                prevvisit = self.GetPositionInfo(self.x + self.dx[d], self.y + self.dy[d])
                if prevvisit == None:
                    locationtype = intcode.RunIntcode(d)
                    grid.SavePositionInfo(d, locationtype)
                    if locationtype != 0:
                        adj += 1
                        intcode.RunIntcode(self.reverse[d])
                elif prevvisit != 0:
                    adj += 1

            self.adjacent[(self.x, self.y)] = adj
        return self.adjacent[(self.x, self.y)]



    # def SavePositionHistory(self, deadend = False):
    def SavePositionHistory(self, adjacent):
        if (self.x, self.y) in self.history:
            self.history[(self.x, self.y)] += 1
        else:
            self.history[(self.x, self.y)] = 1

        if adjacent == 1 and self.history[(self.x, self.y)] < 2:
            self.history[(self.x, self.y)] = 2
        

    def IdentifyNextMove(self):
        # This returns one possible option
        discard = list()

        for poss in self.moves:
            # Dicard possible moves if we already know it's a wall
            if self.GetPositionInfo(self.x + self.dx[poss], self.y + self.dy[poss]) == 0:
                discard.append(poss)

        options = {x: self.GetPositionHistory(self.x + self.dx[x], self.y + self.dy[x]) for x in self.moves if x not in discard}   # could do set(a) - set(b) but harldy worth it
        print(f'Movement options: {options}')
        # sort by value then return key
        options_sorted = sorted(options.items(), key=lambda x: x[1])
        v1, v2 = options_sorted.pop(0)
        if v2 == 0:
            self.move_counter += 1
        else:
            self.move_counter -= 1
        
        print(f'Move counter: {self.move_counter}')

        return v1


    def SavePositionInfo(self, direction, locationtype):
        self.map[(self.x + self.dx[direction], self.y + self.dy[direction])] = locationtype


    def GetPositionInfo(self, x, y):
        # Get the info for any x and y position
        if (x, y) in self.map:
            return self.map[(x, y)]
        else:
            return None



    def GetPositionHistory(self, x, y):
        # Get the info for any x and y position
        if (x, y) in self.history:
            return self.history[(x, y)]
        else:
            return 0


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
locationtype = intcode.RunIntcode()
grid = GridMap()
i = 0

# for i in range(5000):
while locationtype != 2:
    i += 1
    print(f'\nCycle {i}')
    print(f'Current position: {grid.x}, {grid.y}')

    # print(f'Adjacent open squares: {grid.MapSurroundingSquares()}')
    adjacent = grid.MapSurroundingSquares()
    grid.SavePositionHistory(adjacent)

    move = grid.IdentifyNextMove()
    print(f'move: {move}')
    locationtype = intcode.RunIntcode(move)

    # if grid.move_counter != i:
    #     print('BREAK')
    #     break

    if locationtype != 0:
        grid.Move(move)
        if locationtype == 2:
            print(f'Found target: {grid.x}, {grid.y}')
    else:
        print('Wall')

    # print(grid.x, grid.y)
    # print(f'adjacent: {grid.adjacent}\nmap: {grid.map}\nhistory: {grid.history}')
    # print(f'History: {grid.history}\n\n')

grid.PrintGrid()
print(f'Total moves: {grid.move_counter}')
print(f'History: {len(grid.history)}')
print(f'Invalid: {grid.invalid}')
