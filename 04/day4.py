file  = open("input.txt", "r")
lines = file.readlines()

pair = []
for x in lines:
    i = x.replace("\n", "").split(",")
    for y in i:
        pair.append(y.split("-"))

li = []
for x in range(0, len(pair), 2):
    li.append([pair[x][0], pair[x][1], pair[x + 1][0], pair[x + 1][1]])

total  = 0
total2 = 0
for x in li:
    # part One
    a1 = int(x[0]); a2 = int(x[1]); b1 = int(x[2]); b2 = int(x[3])
    if (a1 <= b1 and a2 >= b2) or (a1 >= b1 and a2 <= b2):
        total += 1

    # part Two
    overlap = []
    for i in range(b1, b2 + 1):
        overlap.append(i)
    for i in range(a1, a2 + 1):
        if i in overlap:
            total2 += 1
            break

print(total)
print(total2)