# Working intcode class
# To use need to instatiate and then call RunIntocode() method
# Will display output and prompt for input

class Intcode:

    def __init__(self):
        self.data = [int(x) for x in open('input.txt').read().split(',')]
        self.relbase = 0
        self.i = 0



    def ExtendListLength(self, pointer):
        """ Ensure that the read and write locations exist (set to 0 if not). Called by GetValue for read and WriteCorrectLocation for write. """
        if pointer >= len(self.data):
            for _ in range(len(self.data), pointer+1, 1):
                self.data.append(0)
        pass


    def WriteCorrectLocation(self, pointer, mode, value):
        """ For operations where there is a write ensure that the list is long enough and then do the write to the appropriate location."""
        # Currently only have mode 0 and mode 2 writes
        if mode == 2:
            pointer += self.relbase

        self.ExtendListLength(pointer)
        self.data[pointer] = value



    def GetValue(self, pointer, mode):
        if mode == 0:
            self.ExtendListLength(self.data[pointer])
            return int(self.data[self.data[pointer]])
        elif mode == 1:
            return int(self.data[pointer])
        elif mode == 2:
            self.ExtendListLength(self.data[pointer] + self.relbase)
            return int(self.data[self.data[pointer] + self.relbase])



    def RunIntcode(self):
        while self.data[self.i] != 99:
            opcode = '{:0>5}'.format(self.data[self.i])
            op = int(opcode[3:])
            

            if op == 1:
                v1 = self.GetValue(self.i+1, int(opcode[2]))
                v2 = self.GetValue(self.i+2, int(opcode[1]))
                self.WriteCorrectLocation(self.data[self.i+3], int(opcode[0]), v1+v2)
            elif op == 2:
                v1 = self.GetValue(self.i+1, int(opcode[2]))
                v2 = self.GetValue(self.i+2, int(opcode[1]))
                self.WriteCorrectLocation(self.data[self.i+3], int(opcode[0]), v1*v2)
            elif op == 3:
                j = int(input('Please enter code '))
                self.WriteCorrectLocation(self.data[self.i+1], int(opcode[2]), j)
            elif op == 4:
                v1 = self.GetValue(self.i+1, int(opcode[2]))
                print('Output: ', v1)
            elif op == 5:
                v1 = self.GetValue(self.i+1, int(opcode[2]))
                v2 = self.GetValue(self.i+2, int(opcode[1]))
                self.i = (v2 if v1 != 0 else self.i + 3)
            elif op == 6:
                v1 = self.GetValue(self.i+1, int(opcode[2]))
                v2 = self.GetValue(self.i+2, int(opcode[1]))
                self.i = (v2 if v1 == 0 else self.i + 3)
            elif op == 7:
                v1 = self.GetValue(self.i+1, int(opcode[2]))
                v2 = self.GetValue(self.i+2, int(opcode[1]))
                self.WriteCorrectLocation(self.data[self.i+3], int(opcode[0]), (1 if v1 < v2 else 0))
            elif op == 8:
                v1 = self.GetValue(self.i+1, int(opcode[2]))
                v2 = self.GetValue(self.i+2, int(opcode[1]))
                self.WriteCorrectLocation(self.data[self.i+3], int(opcode[0]), (1 if v1 == v2 else 0))
            elif op == 9:
                v1 = self.GetValue(self.i+1, int(opcode[2]))
                self.relbase += v1

            if op in [1,2,7,8]:
                self.i += 4
            elif op in [3,4,9]:
                self.i += 2

iii = Intcode()
iii.RunIntcode()