# day 16, part 2


iterations = 100



def GetInput():
    data = [int(x) for x in open('input.txt').read() if x != '\n']
    # test = '03036732577212944063491565474664'
    # data = [int(x) for x in test]
    # bigdata = data * 10000

    return data



def RowBaseArray(rowno):
    '''
        Given a rowno return the base pattern unrepeated for use in testing.
        Do not strip off the leading 0.
        The first row = 1.
    '''

    base = [0, 1, 0, -1]
    rowbase = [b for b in base for i in range(rowno)]
    return rowbase



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







def LimitedRowExpansion(input, rowno, halfsum, additional):
    '''
        If halfsum is true then count the whole sum for rowno cycles. Otherwise 0.
        (So for row 4 count 4 iterations. Iterations 5-8 sum to -1*(row 1-4).)
        The do a further additional number of cycles and add to prev value
    '''

    row_sum = 0
    base = RowBaseArray(rowno)
    b = 1

    if halfsum == True:
        for i in range(rowno):
            for j in range(len(input)):
                row_sum = row_sum + (input[j] * base[b])
                b = b + 1 if b < len(base)-1 else 0
        row_sum = row_sum * -1

    for i in range(additional):
        for j in range(len(input)):
            row_sum = row_sum + (input[j] * base[b])
            b = b + 1 if b < len(base)-1 else 0


    return row_sum




def TryMain(input):
    answer = []

    # print(f'Answer: {answer}\ninput: {input}')

    for rowno in range(1, 651):
        b = 1

        half_cycles = 10000 // rowno
        remainder = 10000 % rowno

        # print(f'\nRow: {rowno}\tHalves: {half_cycles}\tRemainder: {remainder}', end = "\t")

        if (half_cycles % 2 == 0) and (remainder == 0):
            row_sum = 0

        if (half_cycles % 2 == 1) and (remainder == 0):
            # row_sum = sum for first rowno values
            row_sum = LimitedRowExpansion(input, rowno, halfsum=True, additional=0)

        if (half_cycles % 2 == 0) and (remainder != 0):
            row_sum = LimitedRowExpansion(input, rowno, halfsum=False, additional=remainder)

        if (half_cycles % 2 == 1) and (remainder != 0):
            row_sum = LimitedRowExpansion(input, rowno, halfsum=True, additional=remainder)

        # print(f'Row Sum: {row_sum}')

        row_value = int(str(row_sum)[-1])
        answer.append(row_value)
        return_value = answer.copy()

    # print(f'Answer: {answer}')
    return return_value





def FindFinalValue(answer):
    '''
    The first seven digits of your initial input signal also represent the message offset. The message offset is the location of the eight-digit message in the final output list. 
    Specifically, the message offset indicates the number of digits to skip before reading the eight-digit message. 
    For example, if the first seven digits of your initial input signal were 1234567, the eight-digit message would be the eight digits after skipping 1,234,567 digits of the final output list.
    '''

    input = GetInput()
    start = [str(i) for i in input[:7]]
    start = int(''.join(start))
    
    # start is now the an integer of the number of digits to skip

    full_cycles = start // 650
    repeated = answer * (full_cycles + 1)
    return repeated[start: start+8]



input = GetInput();

for i in range(iterations):
    input = TryMain(input)

final_answer = FindFinalValue(input)
print(f'The final solution is: {final_answer}')

# The answer is lower than [6, 8, 3, 6, 4, 5, 3, 3]
# Also lower than 6, 2, 7, 2, 2, 5, 1, 5