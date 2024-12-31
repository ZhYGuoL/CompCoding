# N, M = map(int, input().split())

# cows = []
# for _ in range(N):
#     s, t, c = map(int, input().split())
#     cows.append((s, t, c))

# aircon = []
# for _ in range(M):
#     a, b, p, m = map(int, input().split())
#     aircon.append((a, b, p, m))

# cost = 0
# for s, t, c in cows:
#     min_cost = 10000000000
#     for a, b, p, m in aircon:
#         if s <= a <= t or s <= b <= t:
#             if p >= c and m < min_cost:
#                 min_cost = m
#     cost += min_cost
# print(cost)


# n, m = map(int, input().split())
# cows = []
# for i in range(n):
#     s, t, c = map(int, input().split())
#     cows.append((s, t, c))
# aircon = []
# for i in range(m):
#     a, b, p, cost = map(int, input().split())
#     aircon.append((a, b, p, cost))
# cost = 0
# for s, t, c in cows:
#     min_cost = float('inf')
#     for a, b, p, aircon_cost in aircon:
#         if s <= a <= t or s <= b <= t:
#             if p >= c:
#                 print(12)
#                 min_cost = aircon_cost
#     cost += min_cost
#     print(cost)
# print(cost)




# import sys
# from itertools import combinations

# def find_cost(cows, air_conditioners, combination):
#     cost = 0
#     stalls = [0] * 100
#     for i in combination:
#         air_conditioner = air_conditioners[i]
#         cost += air_conditioner[3]
#         for j in range(air_conditioner[0]-1, air_conditioner[1]):
#             stalls[j] = max(stalls[j], air_conditioner[2])
#     for cow in cows:
#         for j in range(cow[0]-1, cow[1]):
#             if stalls[j] < cow[2]:
#                 return sys.maxsize
#     return cost

# def solve(cows, air_conditioners):
#     min_cost = sys.maxsize
#     for i in range(1, 11):
#         for combination in combinations(range(len(air_conditioners)), i):
#             cost = find_cost(cows, air_conditioners, combination)
#             min_cost = min(min_cost, cost)
#     return min_cost

# def main():
#     n, m = map(int, input().split())
#     cows = [list(map(int, input().split())) for i in range(n)]
#     air_conditioners = [list(map(int, input().split())) for i in range(m)]
#     print(solve(cows, air_conditioners))

# if __name__ == '__main__':
#     main()



# import sys
# from itertools import combinations

# def air_conditioner(n, m, cows, conditioners):
#     result = sys.maxsize
#     for comb in combinations(conditioners, m):
#         c = [0] * 101
#         cost = 0
#         for con in comb:
#             for i in range(con[0], con[1]+1):
#                 c[i] = max(c[i], con[2])
#             cost += con[3]
#         flag = True
#         for cow in cows:
#             for i in range(cow[0], cow[1]+1):
#                 if c[i] < cow[2]:
#                     flag = False
#                     break
#             if not flag:
#                 break
#         if flag:
#             result = min(result, cost)
#     return result

# n, m = map(int, input().split())
# cows = []
# for i in range(n):
#     s, t, c = map(int, input().split())
#     cows.append([s, t, c])
# conditioners = []
# for i in range(m):
#     a, b, p, cost = map(int, input().split())
#     conditioners.append([a, b, p, cost])
# print(air_conditioner(n, m, cows, conditioners))




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