import re, collections

# This module creates the equations extracted from the input file.
# It then creates a dictionary of levels below
#
#
#   equations - a dictionary in the form:
#   {
#       'FUEL': {'count': 1, 'components': {'A': 7, 'E': 1}}
#       'E': {'count': 1, 'components': {'A': 7, 'D': 1}}
#   }


equations = dict()
def ExtractEquations(row):
    # Given one line of the input separate it into a dictionary
    # Return product, count of product, dict of components

    # Split the row into the characters up to the arrow (=>) then split those into components
    leftside = row.split('=')[0]
    components = re.findall("\d+ \w+", leftside)
   
    # Arrange the left side components (eg 77 HUYT) into a dict in the format component: number
    # Reverse each string (HUYT 77) so that the letters become the key, then split at space.
    d = dict()
    d = dict(reversed(x.split(' ')) for x in components)

    # Find the products on the right side of the arrow
    out = re.findall("\d+ \w+$", row)[0]
    out_count, out_prod = out.split(' ')

    return out_prod, out_count, d

data = [x for x in open('input.txt').read().split('\n')]
for line in data:
    key, value, components = ExtractEquations(line)
    equations[key] = {'count': value, 'components': components}



# Now create the levels
# ORE is the base level - 0
# level 1 is the elements created from ORE
# level 2 is the elements created from level 1
#
# The purpose of this to ensure the highest levels are expanded first, especially when doing inefficient expansions
# An ineffectient expansion creates a surplus of material so we only want to do that if we know no other item will create it
# We need to start processing with the highest level to ensure the expansions are done in the correct order to make the least possible surplus



levels = {'ORE': 0}
user = list()

def BuildLevels(levels, counter):
    current_level = [element for element, level in levels.items() if level == counter]

    if len(current_level) > 0:
        counter += 1

        for item in current_level:
            for eq in equations:
                if item in equations[eq]['components']:
                    levels[eq] = counter
        BuildLevels(levels, counter)

BuildLevels(levels, 0)
