data = [int(x) for x in open('input.txt').read().split(',')]
jump = {1:4, 2:4, 3:2, 4:2}

i = 0
while data[i] != 99:
    opcode = '{:0>4}'.format(data[i])
    op = int(opcode[2:])

    if op == 1:
        v1 = (data[data[i+1]] if int(opcode[1]) == 0 else data[i+1])
        v2 = (data[data[i+2]] if int(opcode[0]) == 0 else data[i+2])
        data[data[i+3]] = v1 + v2
    elif op == 2:
        v1 = data[data[i+1]] if int(opcode[1]) == 0 else data[i+1]
        v2 = data[data[i+2]] if int(opcode[0]) == 0 else data[i+2]
        data[data[i+3]] = v1 * v2
    elif op == 3:
        j = int(input('Please enter code '))
        data[data[i+1]] = j
    elif op == 4:
        v1 = data[data[i+1]] if int(opcode[1]) == 0 else data[i+1]
        if v1 != 0: print('Output: ', v1)

    if op < 3:
        i += 4
    else:
        i += 2

print('Finished')
