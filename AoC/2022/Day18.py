raw = open("Day18Input.txt").read().split("\n")
coords = set()
for line in raw:
    coords.add(line)
print(coords)