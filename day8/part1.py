data = [int(x) for x in open('input.txt').read().rstrip()]
lines = [data[i:i+150] for i in range(0,len(data),150)]

# Create a list of no of zeros per line
zerocount = [line.count(0) for line in lines]

# Find the line with the lowest no of zeros
low_position = zerocount.index(min(zerocount))

print('Verification sum: ', lines[low_position].count(1) * lines[low_position].count(2))