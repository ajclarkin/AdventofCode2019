# Starting withn part1 from day9 which is a complete computer


data = [int(x) for x in open('input.txt').read().split(',')]
# data = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
# data = [1102,34915192,34915192,7,4,7,99,0]
# data = [104,1125899906842624,99]

relbase = 0

class SpaceshipHull:
    def __init__(self):
        self.outputs = []
        self.position = (0, 0)
        self.point = 'U'
        self.unique_positions = set()
        self.positions = list()
        self.whitespots = {(0,0)}



    def ProcessOutputs(self):
        self.unique_positions.add(self.position)
        self.positions.append(self.position)
        if self.outputs[0] == 1:
            self.whitespots.add(self.position)
        else:
            self.whitespots.discard(self.position)


        turn_left = {'L':'D', 'D':'R', 'R':'U', 'U':'L'}
        turn_right = {'L':'U', 'U':'R', 'R':'D', 'D':'L'}


        if self.outputs[1] == 0:
            # left turn
            self.point = turn_left[self.point]
        else:
            self.point = turn_right[self.point]


        # Now do the move
        dx = {'L':-1, 'D':0, 'R':1, 'U':0}
        dy = {'L':0, 'D':1, 'R':0, 'U':-1}
        x, y = self.position
        self.position = (x + dx[self.point], y + dy[self.point])
        # print(f'({x},{y}) -> {self.position}')

        # Tidy up
        self.outputs.pop(1)
        self.outputs.pop(0)
        return




    def AddOutput(self, output):
        """ Called when the program generates a new output """
        self.outputs.append(output)

        if len(self.outputs) % 2 == 0:
            self.ProcessOutputs()


    def GetPaintColour(self):
        if self.position in self.whitespots:
            return 1
        else:
            return 0




def ExtendListLength(pointer):
    """ Ensure that the read and write locations exist (set to 0 if not). Called by GetValue for read and WriteCorrectLocation for write. """
    global data
    if pointer >= len(data):
        for i in range(len(data), pointer+1, 1):
            data.append(0)
    pass


def WriteCorrectLocation(pointer, mode, value):
    """ For operations where there is a write ensure that the list is long enough and then do the write to the appropriate location."""
    global relbase, data
    # Currently only have mode 0 and mode 2 writes
    if mode == 2:
        pointer += relbase

    ExtendListLength(pointer)
    data[pointer] = value



def GetValue(pointer, mode):
    global relbase, data
    if mode == 0:
        ExtendListLength(data[pointer])
        return int(data[data[pointer]])
    elif mode == 1:
        return int(data[pointer])
    elif mode == 2:
        ExtendListLength(data[pointer] + relbase)
        return int(data[data[pointer] + relbase])


ss = SpaceshipHull()

i = 0
while data[i] != 99:
    opcode = '{:0>5}'.format(data[i])
    op = int(opcode[3:])
    

    if op == 1:
        v1 = GetValue(i+1, int(opcode[2]))
        v2 = GetValue(i+2, int(opcode[1]))
        WriteCorrectLocation(data[i+3], int(opcode[0]), v1+v2)
    elif op == 2:
        v1 = GetValue(i+1, int(opcode[2]))
        v2 = GetValue(i+2, int(opcode[1]))
        WriteCorrectLocation(data[i+3], int(opcode[0]), v1*v2)
    elif op == 3:
        # j = int(input('Please enter code '))
        j = ss.GetPaintColour()
        WriteCorrectLocation(data[i+1], int(opcode[2]), j)
    elif op == 4:
        v1 = GetValue(i+1, int(opcode[2]))
        # print('Output: ', v1)
        ss.AddOutput(v1)
    elif op == 5:
        v1 = GetValue(i+1, int(opcode[2]))
        v2 = GetValue(i+2, int(opcode[1]))
        i = (v2 if v1 != 0 else i + 3)
    elif op == 6:
        v1 = GetValue(i+1, int(opcode[2]))
        v2 = GetValue(i+2, int(opcode[1]))
        i = (v2 if v1 == 0 else i + 3)
    elif op == 7:
        v1 = GetValue(i+1, int(opcode[2]))
        v2 = GetValue(i+2, int(opcode[1]))
        WriteCorrectLocation(data[i+3], int(opcode[0]), (1 if v1 < v2 else 0))
    elif op == 8:
        v1 = GetValue(i+1, int(opcode[2]))
        v2 = GetValue(i+2, int(opcode[1]))
        WriteCorrectLocation(data[i+3], int(opcode[0]), (1 if v1 == v2 else 0))
    elif op == 9:
        v1 = GetValue(i+1, int(opcode[2]))
        relbase += v1

    if op in [1,2,7,8]:
        i += 4
    elif op in [3,4,9]:
        i += 2

print('Finished')
print(f'Unique positions: {len(ss.unique_positions)}')

# Part 2
x_min = x_max = y_min = y_max = 0
x_min = min([pos[0] for pos in ss.positions])
x_max = max([pos[0] for pos in ss.positions])
y_min = min([pos[1] for pos in ss.positions])
y_max = max([pos[1] for pos in ss.positions])

print(f'Range:\nx {x_min} to {x_max}\ny {y_min} to {y_max}')

for y in range(y_min, y_max+1,1):
    line = ''
    for x in range(x_min, x_max+1,1):
        if (x,y) in ss.whitespots:
            line += '#'
        else:
            line += '.'
    print(line)