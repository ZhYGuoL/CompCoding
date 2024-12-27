# a = (open("Day4Input").read().splitlines()[0].split(","))

# print(a)
# print(len(a))

# for i in range(len(a),0,-5):
#     print(i)


numbers = None
AllBoards = []
F = []
board = []
raw = (open("Day4Input").readlines())

nums = raw[0].strip().split(",")

# print(nums)
for line in open("Day4Input"):
    
    line = line.strip()
    print(line)
    if numbers is None:
        numbers = [int(x) for x in line.split(',')]
        print(line)
    else:
        if line:
            board.append([int(x) for x in line.split()])
        else:
            if board:
                AllBoards.append(board)
            board = []
AllBoards.append(board)
print(board)
print("\n")
print(AllBoards)
print("\n")

for IndBoard in AllBoards:
    F.append([[False for x in range(5)] for x in range(5)])

WON = [False for x in range(len(AllBoards))]
print(WON)
for num in numbers:
    for i in range(len(AllBoards)):
        for r in range(5):
            for c in range(5):
                if AllBoards[i][r][c] == num:
                    F[i][r][c] = True

        won = False
        for r in range(5):
            ok = True
            for c in range(5):
                if not F[i][r][c]:
                    ok = False
            if ok:
                won = True
        for c in range(5):
            ok = True
            for r in range(5):
                if not F[i][r][c]:
                    ok = False
            if ok:
                won = True
        if won and not WON[i]:
            WON[i] = True
            nwin = len([j for j in range(len(AllBoards)) if WON[j]])
            print(nwin)
            if nwin == 1 or nwin == len(AllBoards):
                unmarked = 0
                for r in range(5):
                    for c in range(5):
                        if not F[i][r][c]:
                            unmarked += AllBoards[i][r][c]
                print(unmarked * num)