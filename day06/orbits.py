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

# Now count the orbits - need to avoid double counting
total = 0
counted = []
for orb in orbits:
    for element in orb:
        if element not in counted:
            counted.append(element)
            total += orb.index(element)
print('New total: ', total)