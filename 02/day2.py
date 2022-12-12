file  = open("input.txt", "r")
lines = file.readlines()

# part One
points   = {"A":1, "X":1, "B":2, "Y":2,"C":3, "Z":3}
total    = 0
total_z  = 0

for x in range(0,len(lines)):
    game = lines[x].split(" ")
    if game[1].endswith("\n"):
        game[1] = game[1].split("\n")[0]

    # wins
    if (game[1] == "X" and game[0] == "C") or (game[1] == "Y" and game[0] == "A") or (game[1] == "Z" and game[0] == "B"):
        total += points[game[1]] + 6
       
    # lose
    if game[1] == "X" and game[0] == "B" or (game[1] == "Y" and game[0] == "C") or (game[1] == "Z" and game[0] == "A"):
        total += points[game[1]]

    # tie games
    if points[game[1]] == points[game[0]]:
        total += points[game[1]] + 3

    #part2 win-tie-loss
    if game[1] == "X":
        if game[0] == "A":
            total_z += points["Z"]
        if game[0] == "B":
            total_z += points["X"]
        if game[0] == "C":
            total_z += points["Y"]
    
    if game[1] == "Y":
        total_z += points[game[0]] + 3
    
    if game[1] == "Z":
        if game[0] == "A":
            total_z += points["Y"] + 6
        if game[0] == "B":
            total_z += points["Z"] + 6
        if game[0] == "C":
            total_z += points["X"] + 6
    
print("Total",total,"TotalPart2",total_z)