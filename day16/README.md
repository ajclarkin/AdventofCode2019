# Day 16 - Flawed Frequency Transmission
## Part 1

The given input needs to be multiplied by a base frequency characterwise. So char1 * base1, char2 * base2 and so forth. These are then added and the final digit is the input for the next iteration. This gets done n times where n is the length of the input. Each n then creates a digit for the next iteration.

So, if input is 1234 then n = 4 and we do the multiplication 4 times to get the 4 new digits for the input on the next iteration.

The catch - the base frequency expands with each n.
 - n1: 0, 1, 0, -1
 - n2: 0, 0, 1, 1, (2* each digit)
 - n3: 0, 0, 0, 1, (3* each digit)

The other catch: strip the leftmost 1 character of the base array on each row before starting.

*My Approach*
Make an array (list of lists) with all the multiplication values, expanded to the correct length, and with the leading character removed. Then just go ahead and for each line use this value.

After 100 iterations take the first 8 digits of the answer.


## Part 2
Same but this time input = input * 10,000. Try to run this yourself and you'll run out of memory. (I have proof!)
Also, take the first 7 digits of input, treat as integer and use to find the starting place to read the final answer.

So, we can't use brute force and have to use our brains.

Because of the base sequence [0, 1, 0, -1] there is a nice repeating pattern. We miss out the first digit on the first repetition
and so can expect that the sum for the first iteration of input will not be the same as the second - this would only be the case
if it started in the same place.

Proof:
'''
def MultiplySingleRow(input, rowlist, row = 0):
    # input is the 650 chars from input.txt
    length = len(input)
    # base = [0, 1, 0, -1]
    # base = [0, 0, 1, 1, 0, 0, -1, -1]
    base = [0, 0, 0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
    answer = []
    b = 1

    for j in range(12):

        row_sum = 0
        
        for i in range(length):
            row_sum = row_sum + (input[i] * base[b])
            # print(f'{b} - {base[b]}')
            b = b + 1 if b < len(base)-1 else 0

        print(f'Row sum: {row_sum}')
'''

Running this shows the sum of each 650 char input, repeated 12 times. We can change the base that is used for the mulitplication
to see how this affects things.

The pattern is for n extensions of base (which is equal to the row no and the digit place in the input) the first n values are positive, the next n are the same values but negative, and repeat. So every 2n repetitions the rowsum becomes 0.

TO DO
for each row_no find how many half-sets can be discarded. If even number then no row sum implications, if odd then need a positive
row sum. Then see how many remaining repetitions need to be counted which should be less that the length of a half-set. Add on those values.