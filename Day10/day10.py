data = open("input.txt").read().strip()
lines = [x for x in data.split('\n')]

G = [['?' for _ in range(40)] for _ in range(6)]
p1 = 0
x  = 1
t  = 0

for line in lines:
    words = line.split()
    if words[0] == 'noop':
        t += 1

        # Part Two
        t1 = t-1
        G[t1//40][t1%40] = ('#' if abs(x-(t1%40))<=1 else ' ')
        if t in [20, 60, 100, 140, 180, 220]:
            p1 += x*t
    elif words[0] == 'addx':
        t += 1

        # Part Two
        t1 = t-1
        G[t1//40][t1%40] = ('#' if abs(x-(t1%40))<=1 else ' ')
        if t in [20, 60, 100, 140, 180, 220]:
            p1 += x*t
        t += 1

        
        t1 = t-1
        G[t1//40][t1%40] = ('#' if abs(x-(t1%40))<=1 else ' ')
        if t in [20, 60, 100, 140, 180, 220]:
            p1 += x*t
        x += int(words[1])

print(p1)
for r in range(6):
    print(''.join(G[r]))