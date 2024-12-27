data = open('Day17Input.txt', 'r').read()

print(data)

minX = int((data.split(',')[0].split('=')[1].split('..')[0]))
maxX = int((data.split(',')[0].split('=')[1].split('..')[1]))
minY = int((data.split(',')[1].split('=')[1].split('..')[0]))
maxY = int((data.split(',')[1].split('=')[1].split('..')[1]))

minX, maxX = sorted([minX, maxX])
minY, maxY = sorted([minY, maxY])
posMinY, posMaxY = sorted([abs(minY), abs(maxY)])

print(posMinY, posMaxY)

grid = [['.']*(maxX+1) for _ in range(abs(posMaxY)+1)]


print(grid)

print(minX, maxX, minY, maxY)

gridTarget = [['.']*(maxX-minX+1) for _ in range(abs(abs(maxY)-abs(minY))+1)]
print(gridTarget)




# while(1):
#     for i in range()

#**BELOW FOR TESTING AND VISUALIZATION

xLenTest = []
for i in range(maxX+1):
    xLenTest.append(str(i%10))

print(str(xLenTest))
print(''.join(xLenTest))

for idx, row in enumerate(grid):
    print(''.join(row), idx)