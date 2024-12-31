n = int(input().strip())
array = list(map(int, input().strip().split()))
fmin = float("inf")
total = 0
for i in range(n):
    total += array[i]
    fmin = min(array[i],fmin)

for i in range(int(fmin-1)):
    cur = "R" if i % 2 == 0 else "L"
    for j in range(n):
        array[j] -= 1
        total -= 1
        print(cur, end="")

right = True
for i in range(n-1, -1, -1):
    if array[i] == 1:
        continue
    fmin = array[i]

    j = i
    while j >= 0 and array[j] >= fmin:
        array[j] -= fmin - 1
        j -= 1

    for k in range(int(fmin-1)):
        right = not right
        cur = "R" if right else "L"
        for p1 in range(i, j, -1):
            print(cur, end="")
            total -= 1

    while total > 0:
        print("L", end="")
        total -= 1
