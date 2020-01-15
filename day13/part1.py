# Based on day9 / part1


data = [int(x) for x in open('input.txt').read().split(',')]
# data = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
# data = [1102,34915192,34915192,7,4,7,99,0]
# data = [104,1125899906842624,99]

relbase = 0


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


def ProcessOutputs(tiles, outputs):
    """ Should arrive here with outputs being a list of 3 ints """
    # First let's check for duplicates
    pos = (outputs[0], outputs[1])
    if outputs[2] == 2:
        if pos in tiles:
            print('duplicate')
        else:
            tiles.add(pos)

    for _ in range(3):
        outputs.pop()



tiles = set()
outputs = []
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
        j = int(input('Please enter code '))
        WriteCorrectLocation(data[i+1], int(opcode[2]), j)
    elif op == 4:
        v1 = GetValue(i+1, int(opcode[2]))
        outputs.append(v1)
        if len(outputs) == 3:
            ProcessOutputs(tiles, outputs)
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

print(len(tiles))