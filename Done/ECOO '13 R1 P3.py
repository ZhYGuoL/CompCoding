for _ in range(10):
    board = []
    count = 0
    for _ in range(16):
        board.append([int(x, 16)  if x!='-' else x for x in input()])
    # print(board)
    for i in range(16):
        for j in range(16):
            if board[i][j] == "-":
                for k in range(16):
                    if k not in board[i] and k not in [board[x][j] for x in range(16)] and k not in [board[x][y] for x in range(i//4*4, i//4*4+4) for y in range(j//4*4, j//4*4+4)]:
                        count += 1
                        board[i][j] = k
                        break
                # print(board)
    print(count)
    # for i in range(16):
    #     print("".join([str(x) for x in board[i]]))