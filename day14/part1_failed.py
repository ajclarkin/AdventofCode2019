import re, collections
equations = dict()

# This works for all the test cases but not the actual input. Which is annoying.
# Pretty ugly code though.

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


def GetBaseElements(equations):
    """ Return a list of all the elements created directly from ore """
    base_elements = list()
    for element in equations:
        if 'ORE' in equations[element]['components']:
            base_elements.append(element)
    return base_elements



def ExpandComponent(expansion, element, base_elements, inefficient_expansion, base_expansion):
    """ As far as possible replace element within expansion with the components which create it """
    made_expansion = 0


    if int(expansion[element]) >= int(equations[element]['count']) or inefficient_expansion == 1:
        # Check we have enough to do an expansion
        multiples = int(expansion[element]) // int(equations[element]['count'])
        remainder = int(expansion[element]) % int(equations[element]['count'])

        if inefficient_expansion == 1 and (element not in base_elements or base_expansion == 1):
            if base_expansion == 0:
                print(f'Inefficient expansion: {expansion}')

            if remainder > 0:
                multiples += 1
                remainder = 0

        for item_element, item_count in equations[element]['components'].items():
            if item_element in expansion:
                expansion[item_element] = int(expansion[item_element]) + int(item_count) * multiples
            else:
                expansion.update({item_element: int(item_count) * multiples})
            
        if remainder == 0:
            expansion.pop(element)
        else:
            expansion.update({element: remainder})

        if multiples > 0:
            return 1
        else:
            return 0
    else:
        return 0



data = [x for x in open('input.txt').read().split('\n')]
for line in data:
    key, value, components = ExtractEquations(line)
    equations[key] = {'count': value, 'components': components}

base_elements = GetBaseElements(equations)
expansion = equations['FUEL']['components']

print(f'base: {base_elements}')
while len(expansion) > 1:
    made_expansion = 0
    inefficient_expansion = 0
    base_expansion = 0

    while made_expansion == 0:
        expansion_keys = list(expansion.keys())
        for element in expansion_keys:
            if element != 'ORE':
                made_expansion += ExpandComponent(expansion, element, base_elements, inefficient_expansion, base_expansion)
                if made_expansion:
                    inefficient_expansion = 0
                    base_expansion = 0
        if made_expansion == 0 and inefficient_expansion == 0:
            inefficient_expansion = 1
        elif made_expansion == 0 and inefficient_expansion == 1:
            base_expansion = 1
            print('Set base')




    print(expansion, len(expansion))

    # 270580 - too high