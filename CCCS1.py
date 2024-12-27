import sys



size = int(sys.stdin.readline())
prevTop = False
prevBottom = False
count = 0

topRow = [int(x) for x in sys.stdin.readline().split()]
bottomRow = [int(x) for x in sys.stdin.readline().split()]

for i in range(size):
    # if i == 0:
    #     if topRow[i] and bottomRow[i]:
    #         count += 4
    #         prevTop = True
    #         prevBottom = True

    if i % 2 == 0:
        if topRow[i] and bottomRow[i]:
            count += 4
            if prevTop:
                count -= 2
            if prevBottom:
                count -= 2
            prevTop = True
            prevBottom = True
        elif topRow[i]:
            count += 3
            if prevTop:
                count -= 2
            prevTop = True
            prevBottom = False
        elif bottomRow[i]:
            count += 3
            if prevBottom:
                count -= 2
            prevTop = False
            prevBottom = True
        else:
            prevTop = False
            prevBottom = False
    else:
        if topRow[i]:
            count += 3
            if prevTop:
                count -= 2
            prevTop = True
        else:
            prevTop = False
        if bottomRow[i]:
            count += 3
            if prevBottom:
                count -= 2
            prevBottom = True
        else:
            prevBottom = False

    # print(prevTop)
    # print(prevBottom)
    # print(count)

print(count)