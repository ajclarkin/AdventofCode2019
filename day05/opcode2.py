# I did not like this challenge

data = [int(x) for x in open('input.txt').read().split(',')]

def GetValue(pointer, mode):
    if mode == 0:
        return int(data[data[pointer]])
    else:
        return int(data[pointer])

i = 0
while data[i] != 99:
    opcode = '{:0>4}'.format(data[i])
    op = int(opcode[2:])
    

    if op == 1:
        # v1 = (data[data[i+1]] if int(opcode[1]) == 0 else data[i+1])
        v1 = GetValue(i+1, int(opcode[1]))
        v2 = GetValue(i+2, int(opcode[0]))
        data[data[i+3]] = v1 + v2
    elif op == 2:
        v1 = GetValue(i+1, int(opcode[1]))
        v2 = GetValue(i+2, int(opcode[0]))
        data[data[i+3]] = v1 * v2
    elif op == 3:
        j = int(input('Please enter code '))
        data[data[i+1]] = j
    elif op == 4:
        v1 = data[data[i+1]] if int(opcode[1]) == 0 else data[i+1]
        # if v1 != 0: print('Output: ', v1)
        print('Output: ', v1)
    elif op == 5:
        v1 = GetValue(i+1, int(opcode[1]))
        v2 = GetValue(i+2, int(opcode[0]))
        i = (v2 if v1 != 0 else i + 3)
    elif op == 6:
        v1 = GetValue(i+1, int(opcode[1]))
        v2 = GetValue(i+2, int(opcode[0]))
        i = (v2 if v1 == 0 else i + 3)
    elif op == 7:
        v1 = GetValue(i+1, int(opcode[1]))
        v2 = GetValue(i+2, int(opcode[0]))
        data[data[i+3]] = (1 if v1 < v2 else 0)
    elif op == 8:
        v1 = GetValue(i+1, int(opcode[1]))
        v2 = GetValue(i+2, int(opcode[0]))
        data[data[i+3]] = (1 if v1 == v2 else 0)

    if op in [1,2,7,8]:
        i += 4
    elif op in [3,4]:
        i += 2

print('Finished')
