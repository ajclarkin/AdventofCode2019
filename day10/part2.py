from math import atan2, pi, sqrt

data = [x for x in open('input.txt').read() if x != '\n']
# data = [x for x in open('testinput.txt').read() if x != '\n']

def GetCoordinate(i):
    """ Given the index of an item in the original list, return (x, y) """
    dim_x = 20
    dim_y = 20
    return (i % dim_x, i // dim_y)


def CalculateDirectionDistance(p1, p2):
    """ Calculate the x and y distance between two points and then the angle using arctan (inverse tan)
            Arctan returns radians so convert to degrees.
            Arctan x-axis = 0, y-axis =-90; here we add 90 to make y-axis = 0
            Note that y starts at top and works downwards """
    
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    degrees = (atan2(y, x) * 180/pi)
    degrees = degrees + (450 if degrees < -90 else 90)

    distance = sqrt(x **2 + y **2)

    return degrees, distance, p2


current = 328       # this is the asteroid we found in part 1
# current = 271
z = 0
found = []
curr_coord = GetCoordinate(current)

# Check each asteroid that is not the current one we are standing on and save the direction and range
for i in range(len(data)):
    if data[i] == '#' and i != current:
        z+=1
        dest_coord = GetCoordinate(i)
        found.append(CalculateDirectionDistance(curr_coord, dest_coord))

found.sort()

counter = 1
prevbrearing = 0
found[0] = []
for j in range(1,len(found)):
    if found[j][0] != prevbrearing:
        prevbrearing = found[j][0]
        counter += 1
        print(f'{counter}\t{found[j]}')

        if counter == 200:
            print(f'Asteroid 200: {found[j]}')
            x, y = found[j][2]
            print(f'Solution: {x*100 + y}')

        found[j] = []


