seats=list(line for line in (open("Day5Input").read().split("\n")))
biggestID = 0
minFront = 128
maxBack = 0
IDs = []
for seat in seats:  

    back, front = 0, 128
    left, right = 0, 8
    
    for i in range(len(seat)-4):

        if (seat[i]=='B'):
            back += int((front - back)/2)
        else:
            front -= int((front - back)/2)

    if seat[6] == 'B':
        row = front-1
    else:
        row = back

    maxBack, minFront = max(maxBack, back), min(minFront, front)

    for i in range(7, len(seat)):

        if (seat[i]=='R'):
            left += int((right - left)/2)
        else:
            right -= int((right - left)/2)

    if seat[6] == 'R':
        column = right-1
    else:
        column = left

    ID = row*8+column
    biggestID = max(biggestID, ID)
    IDs.append(ID)

IDs = sorted(IDs)

for i in range(1, len(IDs)):
    if IDs[i-1] + 1 != IDs[i]:
        print(IDs[i-1]+1)
