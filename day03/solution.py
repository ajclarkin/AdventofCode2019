# jonathan_paulson's solution from reddit

A,B,_ = open('3.in.txt').read().split('\n')
A,B = [x.split(',') for x in [A,B]]

DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}

def get_points(A):
    x = 0
    y = 0
    length = 0
    ans = {}

    for cmd in A:
        d = cmd[0]
        n = int(cmd[1:])
        assert d in ['L', 'R', 'U', 'D']        # could also do assert d in 'LRUD' because strings and lists are iterable
        for _ in range(n):      # use _ if you don't care about the result
            x += DX[d]
            y += DY[d]
            length += 1
            if (x,y) not in ans:
                ans[(x,y)] = length

    return ans

PA = get_points(A)
PB = get_points(B)

both = set(PA.keys())&set(PB.keys())    # need to understand this
print([(x,y) for (x,y) in both])

part1 = min([abs(x)+abs(y) for (x,y) in both])
part2 = min([PA[p]+PB[p] for p in both])

print(part1, part2)