# Based on day9 / part1
from os import system

data = [int(x) for x in open('input.txt').read().split(',')]
data[0] = 2

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



class ArcadeGame:
    def __init__(self):
        self.blocks = set()
        self.score = 0

        # map is a list of lists saving the game state
        # note that is is addressed as map[y-coord][x-coord] - whereas pos is (x, y)
        self.map = [['' for x in range(37)] for b in range(22)]
        
        # Save the previous position of ball and paddle as these should be set to empty when the object moves
        self.prevball = ()
        self.prevpaddle = ()
        self.paddle_target = 0

        # Will print absolute coordinates if set to 1
        self.debug = 0

        # Set this to 1 to display the game board - adds a lot of run time
        self.display = 0


    def UpdatePaddlePosition(self, pos):
        """ When the ball is moving towards the baseline move the paddle (via the joystick) towards it """
        # The y position is always 20
        x_new, y_new = pos

        if self.prevpaddle != ():
            x_old, y_old = self.prevpaddle
            self.map[y_old][x_old] = '.'


        self.map[y_new][x_new] = '='
        self.prevpaddle = pos

        if self.debug == 1: print(f'\t\t\tPaddle: {pos}')



    def UpdateBallPosition(self, pos):
        # Note that the paddle y position is always 20
        x_new, y_new = pos

        if self.prevball != ():
            x_old, y_old = self.prevball

            # Where the ball was before should now be empty
            self.map[y_old][x_old] = '.'
            if pos in self.blocks:
                self.blocks.remove(pos)

            # Now we need to work out how to move the joystick based on the ball movement - save the target 
            # destination for the paddle and then we can move the joystick accordingly when asked for input

            # Is the ball moving towards then baseline?
            # if y_new != y_old:
            # Try to work out where it will hit the baseline
            moves_to_baseline = 19 - y_new

            if x_new > x_old:
                # Ball moving right
                self.paddle_target = x_new + moves_to_baseline
            else:
                self.paddle_target = x_new - moves_to_baseline - 1

        self.map[y_new][x_new] = '@'
        self.prevball = pos

        if self.debug == 1: print(f'Ball: {pos}\tTarget: {self.paddle_target}')



    def ProcessOutputs(self, outputs):
        """ Should arrive here with outputs being a list of 3 ints """
        pos = (outputs[0], outputs[1])

        # update the high score
        if pos == (-1, 0):
            self.score = outputs[2]
        
        else:
            if outputs[2] == 2:     # block
                self.blocks.add(pos)
                # print('Add')
                self.map[outputs[1]][outputs[0]] = '#'

            elif outputs[2] == 0:   # empty
                if pos in self.blocks:
                    self.blocks.remove(pos)
                self.map[outputs[1]][outputs[0]] = '.'

            elif outputs[2] == 4:   # ball
                self.UpdateBallPosition(pos)

            elif outputs[2] == 3:   # paddle
                self.UpdatePaddlePosition(pos)

            elif outputs[2] == 1:   # wall
                self.map[outputs[1]][outputs[0]] = '+'

        for _ in range(3):
            outputs.pop()

        # print the game board
        if self.display == 1:
            system('cls')
            print('\n'.join(''.join(row) for row in self.map))



    def GetJoystickMovement(self):
        """ This returns the x coordinate on the baseline that the paddle should aim for. """
        if self.prevpaddle[0] > self.paddle_target:
            return -1
        elif self.prevpaddle[0] < self.paddle_target:
            return 1
        else:
            return 0




game = ArcadeGame()
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
        # j = int(input('Please enter code '))
        j = game.GetJoystickMovement()
        WriteCorrectLocation(data[i+1], int(opcode[2]), j)
    elif op == 4:
        v1 = GetValue(i+1, int(opcode[2]))
        outputs.append(v1)
        if len(outputs) == 3:
            game.ProcessOutputs(outputs)
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
    elif op == 99:
        i = 0


print(f'Final score: {game.score}')