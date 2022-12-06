file  = open("input.txt", "r")
line = file.readlines()[0]

def solve(line, length):
    for x in range(0,  len(line) - (length - 1)):
        if len(set([line[x + y] for y in range(0, length)])) == length:
            return (x + length)

print("Part1: ", solve(line, 4), "Part2: ", solve(line, 14))