data = open("input.txt").read().strip()
lines = [x for x in data.split('\n')]

H = (0,0)
T = (0,0)
DR = {"L":0,"U":-1,"R":0,"D":1}
DC = {"L":-1,"U":0,"R":1,"D":0}
TPOS = set()
for line in lines:
    d,amt = line.split()
    amt   = int(amt)
    for x in range(amt):
        TPOS.add(T)
        H = (H[0] + DR[d], H[1] + DC[d])
        dr = (H[0]-T[0])
        dc = (H[1]-T[1])

        if abs(dr) <= 1 and abs(dc) <= 1:
            pass
        elif abs(dr) >= 2 and abs(dc) >= 2:
            T = (H[0] - 1 if T[0] < H[0] else H[0] + 1, H[1] - 1 if T[1] < H[1] else H[1] + 1)
        elif abs(dr) >= 2:
            T = (H[0] - 1 if T[0] < H[0] else H[0] + 1, H[1])
        elif abs(dc) >= 2:
            T = (H[0], H[1] - 1 if T[1] < H[1] else H[1] + 1)
        TPOS.add(T)
print(len(TPOS))