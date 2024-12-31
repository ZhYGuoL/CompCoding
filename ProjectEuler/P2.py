total = 0
lastTwo = [1, 2]
while lastTwo[0]+lastTwo[1] < 90:
    nextVal = lastTwo[0]+lastTwo[1]
    if (nextVal) % 2 == 0:
        total += nextVal
    print(nextVal)
    lastTwo.append(nextVal)
    lastTwo.pop(0)
print(total+2)