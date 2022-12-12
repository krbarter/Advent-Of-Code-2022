file  = open("input.txt", "r")
lines = file.readlines()

crates = [["D", "B", "J", "V"], 
["P", "V", "B", "W", "R", "D", "F"], 
["R", "G", "F","L", "D","C", "W","Q"],
["W","J","P","M","L","N","D","B"],
["H","N","B","P","C","S","Q"],
["R","D","B","S","N","G"],
["Z","B","P","M","Q","F","S","H"],
["W","L","F"],
["S","V","F","M","R"]]

crates_2 = [["D", "B", "J", "V"], 
["P", "V", "B", "W", "R", "D", "F"], 
["R", "G", "F","L", "D","C", "W","Q"],
["W","J","P","M","L","N","D","B"],
["H","N","B","P","C","S","Q"],
["R","D","B","S","N","G"],
["Z","B","P","M","Q","F","S","H"],
["W","L","F"],
["S","V","F","M","R"]]

#crates = [["Z","N"],["M","C","D"],["P"]]
#crates_2 = [["Z","N"],["M","C","D"],["P"]]

for x in lines:
    # getting moves
    x.replace("\n", "")
    x = list(x.split(" "))
    ammuont     = int(x[1])
    original    = int(x[3])  - 1
    destination = int(x[-1]) - 1

    # move part One
    for x in range(0, ammuont):
        p = crates[original].pop()
        crates[destination].append(p)

    # move part Two
    crates_2[destination] += crates_2[original][-ammuont::]
    del crates_2[original][-ammuont::]

final = []
for x in crates:
    final.append(x[-1])

final_2 = []
for x in crates_2:
    final_2.append(x[-1])

print(final)
print(final_2)