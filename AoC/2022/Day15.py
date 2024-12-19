from collections import defaultdict

def part2():
    def dist(x, y): return abs(x[0] - y[0]) + abs(x[1] - y[1])
    res = []
    with open("Day15Input.txt") as f:
        res = f.read().split("\n")
    table = {}
    for line in res:
        a, b = line.split(": ")
        a1, b1 = a.split(", ")
        x1, y1 = int(a1.split("=")[-1]), int(b1.split("=")[-1])
        a2, b2 = b.split(", ")
        beacon1, beacon2 = int(a2.split("=")[-1]), int(b2.split("=")[-1])
        table[(x1, y1)] = (beacon1, beacon2)
    x = 0
    y = 0
    limit = 4000000
    items = list(table.items())
    while y < limit:
        ranges = defaultdict(int)
        for i, j in items:
            highest = dist(i, j) - dist(i, (i[0], y))
            if highest < 0:
                continue
            left = max(0, i[0]-highest)
            right = min(limit, i[0]+highest)
            ranges[left] += 1
            ranges[right+1] -= 1
            cur = 0
        for key in sorted(ranges.keys()):
            cur += ranges[key]
            if cur == 0 and key != limit+1:
                print(key*4000000+y)
                return
        y += 1
part2()