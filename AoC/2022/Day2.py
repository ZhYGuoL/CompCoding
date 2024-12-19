raw = open('Day2Input.txt').readlines()
points = 0
for i in range(len(raw)):
    a, b = raw[i].split(" ")
    print(a, b)
    if a == b:
        points += 3
    elif (a == 'A' and b == 'Y') or (a == 'B' and b == "Z") or (a == 'C' and b == 'X'):
        points += 6
    else :
        points += 0

    if b == 'Y':
        points += 2
    elif b == 'Z':
        points += 3
    elif b == 'X':
        points += 1
    print(points)

print(points)