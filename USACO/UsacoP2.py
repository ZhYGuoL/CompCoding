from typing import List

n, m = map(int, input().split())
cows = [list(map(int, input().split())) for _ in range(n)]
acs = [list(map(int, input().split())) for _ in range(m)]

cost = [0] * 101
for i in range(n):
    s, t, c = cows[i]
    for j in range(s, t+1):
        cost[j] = max(cost[j], c)

totalCost = float('inf')
for i in range(1 << m):
    temp = [x for x in cost]
    curCost = 0
    for j in range(m):
        if i & (1 << j):
            a, b, p, c = acs[j]
            curCost += c
            for k in range(a, b+1):
                temp[k] = max(temp[k] - p, 0)

    if all(x == 0 for x in temp):
        totalCost = min(totalCost, curCost)

print(totalCost)