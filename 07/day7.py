from collections import defaultdict
data = open("input.txt").read().strip()
lines = [x for x in data.split('\n')]

path = []
directories = defaultdict(int)
for x in lines:
    command = x.strip().split()
    if command[1] == "cd":
        if command[2] == "..":
            path.pop()
        else:
            path.append(command[2])
    else:
        try:
            for i in range(0,len(path)+1):
                directories["/".join(path[:i])] += int(command[0])
        except:
            pass

# part Two
total_taken  = directories["/"]
need_to_free = total_taken - 40000000

total = 0
total2 = 1000000000 #limit
for k,v in directories.items():
    if v >= need_to_free:
        total2 = min(total2,v)
    if v <= 100000:
        total += v

print("Part1", total, "Part2", total2)