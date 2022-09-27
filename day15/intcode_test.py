from mod_intcode import Intcode

intcode = Intcode()
result = intcode.RunIntcode()
counter = 0

while result != '' and counter < 20:
    counter += 1
    if result == None:
        result = intcode.RunIntcode(3)
    else:
        print(f'result: {result}')
        result = intcode.RunIntcode()

print('Finished')


