input()
cowNames = input()
cowRanges = [int(x) for x in input().split()]
firstLetter = cowNames[0]
posibilities = 0
if firstLetter == "G":
    HIndex = cowNames.find('H')
    for i in range(HIndex):
        if cowNames[i] == "G":
            if cowRanges[i] >= HIndex+1:
                posibilities += 1
    if cowRanges[0] >= HIndex+1:
        print(posibilities)
        exit()
    else:
        if cowRanges[0] >= cowNames.rfind('G')+1:
            print(posibilities+1)
            exit()
    print(posibilities)
else:
    GIndex = cowNames.find('G')
    for i in range(GIndex):
        if cowNames[i] == "H":
            if cowRanges[i] >= GIndex+1:
                posibilities += 1
    if cowRanges[0] >= GIndex+1:
        print(posibilities)
        exit()
    else:
        if cowRanges[0] >= cowNames.rfind('H')+1:
            print(posibilities+1)
            exit()
    print(posibilities)