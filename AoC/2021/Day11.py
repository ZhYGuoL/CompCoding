import itertools
 
grid = []
with open('Day11Input', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        grid.append(line)
 
width, height = len(grid[0]), len(grid)
 
def neighbors(p):
    for d in itertools.product(range(-1, 2), repeat=2):
        if d == (0, 0):
            continue
        x = p[0] + d[0]
        y = p[1] + d[1]
        if (0 <= x < width) and (0 <= y < height):
            yield (x, y)
 
grid = [[int(x) for x in row] for row in grid]
 
cells = width * height
total_flashes = 0
for step in itertools.count(1):
    flashes = 0
    grid = [[x + 1 for x in row] for row in grid]
    stack = [(i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x > 9]
    while stack:
        (i, j) = stack.pop()
        flashes += 1
        for (i1, j1) in neighbors((i, j)):
            grid[i1][j1] += 1
            if grid[i1][j1] == 10:
                stack.append((i1, j1))
    total_flashes += flashes
    if step == 100:
        print(f"Part 1: {total_flashes}")
    if flashes == cells:
        print(f"Part 2: {step}")
        break
    grid = [[0 if x > 9 else x for x in row] for row in grid]