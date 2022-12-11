from copy import deepcopy
data = open('input.txt').read().strip()
lines = [x for x in data.split('\n')]

# storing all operations
M, OP, DIV, TRUE, FALSE = [],[],[],[],[]

for monkey in data.split('\n\n'):
    id_, items, op, test, true, false = monkey.split('\n')
    M.append([int(i) for i in items.split(':')[1].split(',')])
    words = op.split()
    op = ''.join(words[-3:])
    # unique lamda function to store the value of the last 3 point -> equation direct to solution
    OP.append(lambda old,op=op:eval(op))
    DIV.append(int(test.split()[-1]))
    TRUE.append(int(true.split()[-1]))
    FALSE.append(int(false.split()[-1]))

# Passing the deep copy down in two steps
START = deepcopy(M)

# Part2
lcm = 1
for x in DIV:
    lcm = (lcm*x)

# Evaluations of each throw and each respose
for part in [1,2]:
    C = [0 for _ in range(len(M))]
    M = deepcopy(START)
    for t in range(20 if part==1 else 10000):
        for i in range(len(M)):
            for item in M[i]:
                #print(i,item)
                C[i] += 1
                item = OP[i](item)
                # Part Two Done seperate as a percentage
                if part == 2:
                    item %= lcm 
                if part == 1:
                    item = (item // 3)
                if item % DIV[i] == 0:
                    M[TRUE[i]].append(item)
                else:
                    M[FALSE[i]].append(item)
            M[i] = []
    print(sorted(C)[-1] * sorted(C)[-2])