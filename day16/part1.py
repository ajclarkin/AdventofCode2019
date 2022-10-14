# day 16


iterations = 100


def GetInput():
    data = [int(x) for x in open('input.txt').read() if x != '\n']

    # test = 80871224585914546619083218645595
    # data = [int(x) for x in str(test)]

    return data


def MultiplicationPhase(input, rowlist):
    '''
        Given the input value and the rowlist do one series of multiplications.
        Will need to repeat for however many iterations are required.
        Could build in iterations here but nested loops might become mind-boggling.
    '''
    length = len(input)

    answer = []

    for j in range(length):

        row_sum = 0
        row_value = 0
        for i in range(length):
            row_sum = row_sum + (input[i] * rowlist[j][i])

        # input = answer.copy()
        # Row value becomes the (positive) rightmost digit of row_sum
        row_value = int(str(row_sum)[-1])
        answer.append(row_value)

    return answer




def BaseArray(length):
    '''
        For a given length of input calculate the base array which it will be added to.
        For length l the array needs to be l*l.
        The first element needs to be removed from each row so when generating it must be l+1 long.
        
        Returns list of lists making up the base array.
    '''

    base = [0, 1, 0, -1]
    rowlist = []

    for repeats in range(1, length+1):
        row = []    
        b = 0
        while len(row) <= length:           # Keep adding mulitples of characters until length ok
            for i in range(repeats):        # append multiple of character to range
                row.append(base[b])
            b = b+1 if b < 3 else 0
        
        rowlist.append(row[1:length+1])
    return rowlist



input = GetInput();

rowlist = BaseArray(len(input))

for i in range(iterations):
    input = MultiplicationPhase(input, rowlist)

print(input[0:8])