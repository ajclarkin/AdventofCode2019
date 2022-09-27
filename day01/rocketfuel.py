# Advent of Code - Day 1
# Input: file containing a list of module weights as integers
# Process: calculate fuel required for each input entry
# Output = (input / 3) -> round down -> subtract 2
# So: (input // 3) - 2


# Part 2
# Need to add the fuel required to carry the fuel
# For a calculated fuel requirement iterate through the above formula until calc < 0 and add that

inputfile = 'input.txt'
sum = 0
fuel = 0
addfuel = 0

with open(inputfile) as f:
    for line in f:
        # Fuel for the module
        fuel = (int(line)//3)-2
        sum += fuel

        # Fuel for the fuel
        while fuel > 0:
            fuel = (fuel//3)-2
            if fuel > 0:
                sum += fuel

print('Final total:', sum)