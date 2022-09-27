data = [x for x in open('input.txt').read().split('\n')]
# data = [x for x in open('testdata.txt').read().split('\n')]

orbits = []
orbit_count = 0
orbit_current = 0
this_orbit = []

pairs = [x.split(')') for x in data[:-1]]
def Seeker(needle):
    for p in pairs:
        if p[0] == needle:
            pairs.pop(pairs.index(p))
            return p[1]
    return 0


def FinishChain(needle):
    chain = []
    found = Seeker(needle)
    while found != 0:
        chain.append(found)
        needle = found
        found = Seeker(needle)
    return chain



needle = 'COM'
this_orbit.append(needle)
chain = FinishChain(needle)
if len(chain) > 0:
    orbits.append(this_orbit + chain)
    orbit_count += 1

while len(pairs) > 0:
    for o in range(orbit_count):
        for element in orbits[o]:
            chain = FinishChain(element)
            if len(chain) > 0:
                orbits.append(orbits[o][:orbits[o].index(element)+1] + chain)
                orbit_count += 1

# At this point all the orbits exist in orbits[] from COM -> outermost planet
orb1 = [orbits.index(o) for o in orbits if 'YOU' in o]
orb2 = [orbits.index(o) for o in orbits if 'SAN' in o]
o1 = orbits[orb1[0]]
o2 = orbits[orb2[0]]

# Now find the element common to both lists with the highest index

for e in range(len(o1)-1, 0, -1):
    if o1[e] in o2:
        index1 = e
        index2 = o2.index(o1[e])
        break

# Find the distance from the YOU -> common point and SAN-> common point
# then subtract 2 because we actually want the distance from the objects YOU and SAN are orbitting

d1 = o1.index('YOU') - index1
d2 = o2.index('SAN') - index2

print('Distance =', (d1+d2-2))



