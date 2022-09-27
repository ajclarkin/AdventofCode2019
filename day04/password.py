# Find the number of passcodes between min and max that meet criteria
#  - 2 adjacent numbers are the same
#  - left to right digits never decrease, only same or greater

min = 234208
max = 765869
counter = 0


# NEED TO KEEP LOOKING IF ATRIPLET IS FOUND

def CheckForDuplicates(check):
    # check = str(current)
    runs = []
    runcounter = 1
    for i in  range(0,5):
        if check[i] == check[i+1]:
            runcounter += 1
            if i == 4:
                runs.append(runcounter)
        else:
            runs.append(runcounter)
            runcounter = 1

    if 2 in runs:
        return 1
    else:
        return 0


def CheckForAscending(check):
    for i in  range(1,6):
        if int(check[i]) < int(check[i-1]):
            return 0
    return 1




for lcv in range(min, (max+1)):
    if CheckForDuplicates(str(lcv)):
        if CheckForAscending(str(lcv)):
            # print('Found one: ', lcv)
            counter += 1

print('Total matching passwords', counter)
