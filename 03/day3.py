file  = open("input.txt", "r")
lines = file.readlines()

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = 0
total2 = 0

# part One
for x in lines:
    first, second = x[:len(x)//2], x[len(x)//2:]
    same = ''.join(set(first) & set(second))
    total += alpha.find(same) + 1

# part Two
for x in range(0, len(lines) - 2, 3):
    same = ''.join(set(lines[x].split("\n")[0] ) & set(lines[x + 1].split("\n")[0]) & set(lines[x + 2].split("\n")[0]))
    total2 += alpha.find(same) + 1

print("Total:", total, "TotalPart2:", total2)