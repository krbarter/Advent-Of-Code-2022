trees =  [list(map(int,list(row))) for row in open("input.txt").read().split("\n")]
total2 = []

for x in range(1, len(trees) - 1):
    for y in range(1, len(trees[0]) - 1):
        height, row, column = trees[x][y],trees[x],[row[y] for row in trees]
        paths = [row[:y][::-1],row[y+1:],column[:x][::-1],column[x+1:]]
        score = 1
        visibleDir = 0
        for path in paths:
            lookScore = 0
            for tree in path:
                lookScore += 1
                if tree >= height:
                    break
            score *= lookScore
        total2.append(score)

print("Best Scenic Score is: "+ str(max(total2)))