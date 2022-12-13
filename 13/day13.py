from functools import cmp_to_key
data = open('input.txt').read().strip()

def compare(p1,p2):
    if isinstance(p1, int) and isinstance(p2,int):
        if p1 < p2:
            return -1
        elif p1 == p2:
            return 0
        else:
            return 1
    elif isinstance(p1, list) and isinstance(p2, list):
        i = 0
        while i < len(p1) and i < len(p2):
            c = compare(p1[i], p2[i])
            if c== -1:
                return -1
            if c == 1:
                return 1
            i += 1
        if i == len(p1) and i < len(p2):
            return -1
        elif i == len(p2) and i < len(p1):
            return 1
        else:
            return 0
    elif isinstance(p1, int) and isinstance(p2, list):
        return compare([p1], p2)
    else:
        return compare(p1, [p2])

packets = []
total   = 0
total2  = 1

group = data.split('\n\n')
for x in range(len(group)):
    p1,p2 = group[x].split('\n')
    p1,p2 = eval(p1),eval(p2)
    packets.append(p1)
    packets.append(p2)
    if compare(p1, p2) == -1:
        total += x + 1

# Divider packets
packets.append([[2]])
packets.append([[6]])

packets = sorted(packets, key=cmp_to_key(lambda p1,p2: compare(p1,p2)))
for i,p in enumerate(packets):
    if p == [[2]] or p == [[6]]:
        total2 *= i + 1

print(total, total2)