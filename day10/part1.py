from math import atan2, pi

data = [x for x in open('input.txt').read() if x != '\n']
# data = [x for x in open('testinput.txt').read() if x != '\n']

vistotal = {}

def GetCoordinate(i):
    """ Given the index of an item in the original list, return (x, y) """
    dim_x = 20
    dim_y = 20
    return (i % dim_x, i // dim_y)


def CalculateGradient(p1, p2):
    """ Calculate the x and y distance between two points and then the angle using arctan (inverse tan)
            Arctan returns radians so convert to degrees
            Note that y starts at top and works downwards """
    
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    degrees = atan2(y, x) * 180/pi
    return degrees

for current in range(len(data)):
    z = 0
    if data[current] == '#':
        found = set()
        curr_coord = GetCoordinate(current)

        # Check each asteroid that is not the current one we are standing on and save the direction and range
        for i in range(len(data)):
            if data[i] == '#' and i != current:
                z+=1
                dest_coord = GetCoordinate(i)
                grad = CalculateGradient(curr_coord, dest_coord)
                found.add(grad)

        vistotal[current] = len(found)

print(f'The item with the best view is: {max(vistotal, key=vistotal.get)} ({GetCoordinate(max(vistotal, key=vistotal.get))})')
print(f'Maxiumum number is: {max(vistotal.values())}')
