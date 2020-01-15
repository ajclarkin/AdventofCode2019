import re, hashlib
import numpy as np
# note - using numpy which is installed in a venv. advent\scripts\activate.bat to activate


data = [line for line in open('input.txt').read().split('\n')]
# data = [line for line in open('testinput.txt').read().split('\n')]
coordinates = [re.findall("-?\d+", row) for row in data]
universe = set()


class JupiterMoon:
    
    def __init__(self, initial_coords):
        self.x, self.y, self.z = initial_coords
        self.x = self.orig_x = int(self.x)
        self.y = self.orig_y = int(self.y)
        self.z = self.orig_z = int(self.z)
        self.vel_x = self.vel_y = self.vel_z = 0


    def UpdateVelocity(self, dest_coords):

        def CalculateDifference(a, b):
            if b > a:
                return 1
            elif b < a:
                return -1
            else:
                return 0


        self.vel_x = self.vel_x + CalculateDifference(self.x, dest_coords[0])
        self.vel_y = self.vel_y + CalculateDifference(self.y, dest_coords[1])
        self.vel_z = self.vel_z + CalculateDifference(self.z, dest_coords[2])

        # print(self.vel_x, self.vel_y, self.vel_z)


    def ListCoordinates(self):
        return [self.x, self.y, self.z]


    def ListVelocity(self):
        return [self.vel_x, self.vel_y, self.vel_z]


    def UpdatePosition(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.z += self.vel_z


    def CalculateEnergy(self):
        potential = abs(self.x) + abs(self.y) + abs(self.z)
        kinetic = abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z)
        return potential * kinetic


    def Reset(self, initial_coords):
        """ We run the model 3 times to calc x,y and z. Use this to reinitialise the positions and velocities """
        self.__init__(initial_coords)




# Create a list of JupiterMoon objects
moons = [JupiterMoon(entry) for entry in coordinates]




def TestOriginalPosition(moons, dim):
    if dim == 0:
        for m in moons:
            if m.x == m.orig_x and m.vel_x == 0:
                pass
            else:
                return False
        return True

    if dim == 1:
        for m in moons:
            if m.y == m.orig_y and m.vel_y == 0:
                pass
            else:
                return False
        return True

    if dim == 2:
        for m in moons:
            if m.z == m.orig_z and m.vel_z == 0:
                pass
            else:
                return False
        return True


cycles = []
for dim in range(3):
    j=0
    while True:
        for source in moons:
            for dest in (m for m in moons if m != source):
                source.UpdateVelocity(dest.ListCoordinates())

        for source in moons:
            source.UpdatePosition()
        j += 1

        if TestOriginalPosition(moons, dim):
            for x, m in enumerate(moons):
                m.Reset(coordinates[x])
            break

    print(j)
    cycles.append(j)

# note that although python can handle a massive int numpy cannot and so need to use a bigger int type
least_common_multiple = np.lcm.reduce(cycles, dtype=np.int64)

print('The final answer is ', least_common_multiple)
