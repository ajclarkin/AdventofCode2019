import mod_equations

# Space Stoichiometry
# Calculate how much ore is required to create one unit of fuel

equations = mod_equations.equations
levels = mod_equations.levels


def ExpandComponent(expansion, element, inefficient_expansion):
    """ As far as possible replace element within expansion with the components which create it """
    if int(expansion[element]) >= int(equations[element]['count']) or inefficient_expansion:
        # Check we have enough to do an expansion
        multiples = int(expansion[element]) // int(equations[element]['count'])
        remainder = int(expansion[element]) % int(equations[element]['count'])

        if inefficient_expansion == 1:
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


expansion = equations['FUEL']['components']
inefficient_expansion = 0
while len(expansion) > 1:
    break_on_exit = 0
    made_expansion = 0

    expansion_keys = list(expansion.keys())
    for checklevel in range(max(levels.values()), 0, -1):
        toexpand = [e for e in expansion_keys if levels[e] == checklevel and e != 'ORE']
        if len(toexpand) > 0:
            break_on_exit = 1
            while len(toexpand) > 0:
                made_expansion += ExpandComponent(expansion, toexpand.pop(), inefficient_expansion)
                if made_expansion and inefficient_expansion:
                    inefficient_expansion = 0
            else:
                if break_on_exit == 1 and made_expansion:
                    break

    if made_expansion == 0:
        inefficient_expansion = 1
    else:
        inefficient_expansion = 0

print(expansion)


# Correct answer: 261960