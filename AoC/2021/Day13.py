data = open('Day13Input.txt').read().split('\n\n')

updCoods = data[0].split('\n')

xMax, yMax = 0, 0
for coord in updCoods:
    xMax = max(xMax, int(coord.split(',')[0]))
    yMax = max(yMax, int(coord.split(',')[1]))


for i in range(len(data[1].split('\n'))):

    fold = data[1].split('\n')[i].split('=')[0][-1]
    curCoords = updCoods
    updCoods = []

    if fold == 'y':
        yMax = int(yMax/2)-1
        for coord in curCoords:
            x, y = int(coord.split(',')[0]), int(coord.split(',')[1])

            if y > (yMax):
                y = abs((y-int((yMax+2))-int(yMax)))

            updCoods.append(str(x)+','+str(y))
    else:
        xMax = int(xMax/2)-1
        for coord in curCoords:
            x, y = int(coord.split(',')[0]), int(coord.split(',')[1])

            if x > (xMax+1):
                x = abs((x-int((xMax+2))-int(xMax)))

            updCoods.append(str(x)+','+str(y))


grid = [['.'] * (xMax+1) for _ in range(yMax+1)]
for coord in updCoods:
    grid[int(coord.split(',')[1])][int(coord.split(',')[0])] = '#'
    

for row in grid:
    print(''.join(row))




# **BELOW** Part One

# counter = 0

# for i in grid:
#     for a in i:
#         if a == '#':
#             counter+=1

# print(counter)