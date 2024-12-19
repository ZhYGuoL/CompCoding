# raw = open("Day9Input").read().split('\n')

# for i in range(len(raw)):
#     line = raw[i]
#     for n in range(2,len(line)):
#         if int(line[n-2]) > int(line[n-1]) and int(line[n-1]) < int(line[n]):
#             print(line, line[n-1])
#             continue



# raw = [[int(y) for y in x] for x in open('Day9Input').read().strip().split('\n')]
# s=0
# for i in range(len(raw)):
# 	for j in range(len(raw[0])):
# 		if i>0 and raw[i][j] >= raw[i-1][j]:
# 			continue
# 		if i<len(raw)-1 and raw[i][j] >= raw[i+1][j]:
# 			continue
# 		if j>0 and raw[i][j] >= raw[i][j-1]:
# 			continue
# 		if j<len(raw[0])-1 and raw[i][j] >= raw[i][j+1]:
# 			continue
# 		s += raw[i][j]+1
# print(s)


# def bound(x, y):
#     if 0 <= x < n and 0 <= y < m:
#         return True
#     return False

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# for i in range(4):
#     if grid[x + dx[i]][y + dy[i]]:


heights = [[int(c) for c in line.strip()] for line in open("Day9Input", "r").readlines()]
# print(heights)
gridH = len(heights)
gridW = len(heights[0])
# print(gridH, gridW)


def validSurroundings(y, x):
    surroundings = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    return [(a, b) for a, b in surroundings if 0 <= a < gridH and 0 <= b < gridW]



# Part 1
lowPoints = []
for y in range(gridH):
    for x in range(gridW):
        if all(heights[y][x] < heights[a][b] for a, b in validSurroundings(y, x)):
            lowPoints.append((y, x))

# print(sum(heights[y][x] + 1 for y, x in lowpoints))

print(lowPoints)

# Part 2
def get_basin(y, x):
    basin = {(y, x)}
    for a, b in validSurroundings(y, x):
        if heights[a][b] > heights[y][x] and heights[a][b] < 9:
            basin |= get_basin(a, b)
    return basin
        
test = [get_basin(y, x) for y, x in lowPoints]
print(test)
sizes = sorted([len(get_basin(y, x)) for y, x in lowPoints])
print(sizes)
print("Part 2:", sizes[-1] * sizes[-2] * sizes[-3])