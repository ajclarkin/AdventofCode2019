data = [int(x) for x in open('input.txt').read().rstrip()]
lines = [data[i:i+150] for i in range(0,len(data),150)]

output = ''
cont = 1

for charposition in range(150):
    layer = 0
    while layer < 100:
        if lines[layer][charposition] != 2:
            if lines[layer][charposition] == 1:
                output = output + '#'
            else:
                output = output + ' '
            break
        layer += 1
    

for x in range(6):
    print(output[x*25:(x+1)*25])