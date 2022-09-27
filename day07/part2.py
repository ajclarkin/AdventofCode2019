class Amplifier:

    def __init__(self, data, inputs):
        self.data = data
        self.inputs = inputs
        self.i = 0


    def GetValue(self, pointer, mode):
        if mode == 0:
            return int(self.data[self.data[pointer]])
        else:
            return int(self.data[pointer])



    def Intcode(self, newinput):
        outputs = []
        self.inputs = self.inputs + newinput

        while self.data[self.i] != 99:
            opcode = '{:0>4}'.format(self.data[self.i])
            op = int(opcode[2:])
            ready_to_return = 0


            if op == 1:
                # v1 = (data[data[self.i+1]] if int(opcode[1]) == 0 else data[self.i+1])
                v1 = self.GetValue(self.i+1, int(opcode[1]))
                v2 = self.GetValue(self.i+2, int(opcode[0]))
                self.data[self.data[self.i+3]] = v1 + v2
            elif op == 2:
                v1 = self.GetValue(self.i+1, int(opcode[1]))
                v2 = self.GetValue(self.i+2, int(opcode[0]))
                self.data[self.data[self.i+3]] = v1 * v2
            elif op == 3:
                # print('op 3')
                if len(self.inputs) > 0:
                    j = self.inputs.pop(0)
                    self.data[self.data[self.i+1]] = j
                else:
                    ready_to_return = 1
            elif op == 4:
                v1 = self.data[self.data[self.i+1]] if int(opcode[1]) == 0 else self.data[self.i+1]
                outputs.append(v1)
            elif op == 5:
                v1 = self.GetValue(self.i+1, int(opcode[1]))
                v2 = self.GetValue(self.i+2, int(opcode[0]))
                self.i = (v2 if v1 != 0 else self.i + 3)
            elif op == 6:
                v1 = self.GetValue(self.i+1, int(opcode[1]))
                v2 = self.GetValue(self.i+2, int(opcode[0]))
                self.i = (v2 if v1 == 0 else self.i + 3)
            elif op == 7:
                v1 = self.GetValue(self.i+1, int(opcode[1]))
                v2 = self.GetValue(self.i+2, int(opcode[0]))
                self.data[self.data[self.i+3]] = (1 if v1 < v2 else 0)
            elif op == 8:
                v1 = self.GetValue(self.i+1, int(opcode[1]))
                v2 = self.GetValue(self.i+2, int(opcode[0]))
                self.data[self.data[self.i+3]] = (1 if v1 == v2 else 0)



            if ready_to_return == 1:
                return outputs

            if op in [1,2,7,8]:
                self.i += 4
            elif op in [3,4]:
                self.i += 2

        return outputs


data = [int(x) for x in open('input.txt').read().split(',')]
# data = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
final = 0
largest = [] 


# Generate all the phase settings and store in a list
phases = []
for a in range(5,10):
    for b in range(5,10):
        for c in range(5,10):
            for d in range(5,10):
                for e in range(5,10):
                    temp = [a,b,c,d,e]
                    if max([temp.count(t) for t in temp]) == 1: phases.append(temp)



for phase in phases:
    inps = [[phase.pop(0)] for a in range(5)]

    amps = [Amplifier(data[:], inps[j]) for j in range(5)]

    i = 0
    output = [0]

    while output:
        final = output[0]
        output = amps[i].Intcode(output)
        i = i+1 if i<4 else 0

    largest.append(final)

print(f'The largest output: {max(largest)}')