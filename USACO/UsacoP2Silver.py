n = int(input().strip())
grid = [[0] * (n + 1) for i in range(n + 1)]
costs = [[0] * (n + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    s = input().strip()
    for j in range(1, n + 1):
        grid[i][j] = s[j - 1]
        costs[i][j] = 0
for i in range(1, n + 1):
    s = input().strip().split()
    for j in range(1, n + 1):
        costs[i][j] = int(s[j - 1])
q = int(input().strip())
total_cost = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if grid[i][j] == "R":
            total_cost += costs[i][j + 1]
        elif grid[i][j] == "D":
            total_cost += costs[i + 1][j]
print(total_cost)
for i in range(q):
    x, y = map(int, input().strip().split())
    if grid[x][y] == "R":
        grid[x][y] = "D"
        total_cost = total_cost - costs[x][y + 1] + costs[x + 1][y]
    elif grid[x][y] == "D":
        grid[x][y] = "R"
        total_cost = total_cost - costs[x + 1][y] + costs[x][y + 1]
    print(total_cost)
