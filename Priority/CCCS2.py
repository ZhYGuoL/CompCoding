import sys

_ = sys.stdin.readline()
heights = [int(i) for i in sys.stdin.readline().split()]


for size in range(1, len(heights)+1):
    minPic = 11001010101203912039
    if size == 1:
        print(0, end=' ')
        continue
    for index in range(len(heights)-size+1):
        # print(size, index)
        curPic = heights[index:index+size]
        count = 0
        if len(curPic) % 2 == 0:
            for i in range(int(len(curPic)/2)):
                count += abs(curPic[i]-curPic[len(curPic)-i-1])
            minPic = min(minPic, count)
        else:
            for i in range(int((len(curPic)/2))):
                count += abs(curPic[i]-curPic[len(curPic)-i-1])
            minPic = min(minPic, count)

    print(minPic, end=" ")
# remember the min size edgecases
    