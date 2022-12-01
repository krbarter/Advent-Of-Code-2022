import os

file  = open("input.txt", "r")
lines = file.readlines()

# part One
elves = []
total = 0
for x in range(0, len(lines)):
    if lines[x].split("\n")[0] != '':
        total += int(lines[x].split("\n")[0])
    else:
        elves.append(total)
        total = 0

print(max(elves))

# part Two
top3 = 0
sorted = sorted(elves)[::-1]
for i in range(3):
    top3 += sorted[i]

print(top3)