import re

data = [line for line in open('input.txt').read().split('\n')]
# data = [line for line in open('testinput.txt').read().split('\n')]
coordinates = [re.findall("-?\d+", row) for row in data]



class JupiterMoon:
    
    def __init__(self, initial_coords):
        self.x, self.y, self.z = initial_coords
        self.x = int(self.x)
        self.y = int(self.y)
        self.z = int(self.z)
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


    def UpdatePosition(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.z += self.vel_z


    def CalculateEnergy(self):
        potential = abs(self.x) + abs(self.y) + abs(self.z)
        kinetic = abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z)
        return potential * kinetic




# Create a list of JupiterMoon objects
moons = [JupiterMoon(entry) for entry in coordinates]

# For each moon in the system iterate through other moons and calculate velocity 

for i in range(1000):
    for source in moons:
        for dest in (m for m in moons if m != source):
            source.UpdateVelocity(dest.ListCoordinates())

    for source in moons:
        source.UpdatePosition()

energy = 0
for m in moons:
    energy += m.CalculateEnergy()

print(f'The total energy is: {energy}')

