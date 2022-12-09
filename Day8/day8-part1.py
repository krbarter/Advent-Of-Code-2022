import numpy as np

score = []
lines      = np.array([list(x.strip()) for x in open("input.txt")], int)
nrow, ncol = np.shape(lines)
visible    = ncol * 2 + (nrow - 2) * 2

for x in range(1, nrow - 1):
    for y in range(1, ncol - 1):
        # branches  
        tree       = lines[x,y]
        tree_up    = lines[:x,y]
        tree_down  = lines[x + 1:, y]
        tree_right = lines[x, y + 1:]
        tree_left  = lines[x, :y]

        if tree > max(tree_up) or tree > max(tree_down) or tree > max(tree_left) or tree > max(tree_right):
            visible += 1
        
print("Part1", visible)