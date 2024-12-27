# import math

# print(int(-110*(-109)/2))


# data = open('Day17Input.txt', 'r').read().split(',')
# print(data)

# xrange = data[0].split('=')[1].split('..')
# yrange = data[1].split('=')[1].split('..')


# target = (int(min(xrange)), int(max(xrange)), int(min(yrange)), int(max(yrange)))


# #**PRINTS

# print(xrange, yrange)
# print(target)

# print(int(math.sqrt(target[0])))

data = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]


while(1):
    for lineIdx in range(1, len(data)):
        data[lineIdx][1] = 'asd'
        print(data[lineIdx])
        print(data[lineIdx-1])
        break