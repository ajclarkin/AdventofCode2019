# Messing around for part 2

for row in range(1, 41):
    base_length = 4*row

    # if row == 1 then row sum posistive in row 1, negative row 2
    # if row == 2 then row sum posistive in row 1&2, negative row 3&4

    halves = base_length / 4
    print(f'Row {row}\tFull half-repetitions {10000//halves}\tRemaining halfs {10000%halves}')


    