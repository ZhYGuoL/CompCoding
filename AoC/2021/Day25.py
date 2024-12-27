data = open('Day25Input.txt', 'r').read().split('\n')

# print(lines)
# for line in lines:
#     print(line)

same = 0
newlines = data
oldlines = []
iteration = 0

for lineIdx, line in enumerate(newlines):
    newlines[lineIdx] = list(line)

for line in newlines:
    print(''.join(line))

print(newlines)

while same == 0:

    if oldlines == newlines:
        print(iteration)
        break
    print(oldlines)
    print(newlines)
    oldlines = newlines
    print(newlines)
    for lineIdx, line in enumerate(newlines):
        xLenTest = []
        line = list(line)
        justMoved = 0
        for i in range(len(line)):
            xLenTest.append(str(i%10))
        print('\n')
        print('  '+''.join(xLenTest))
        print(lineIdx, ''.join(line))
        for charIdx, char in enumerate(line):
            
            # print(charIdx, char)
            if char == '>':
                print('\n')           
                print(lineIdx, charIdx, char)
                # if justMoved:
                #     justMoved = 0
                #     continue
                if charIdx+1 == len(line):
                    if line[0] == '.':
                        newlines[lineIdx][0] = '>'
                        newlines[lineIdx][charIdx] = '.'
                    print('overflow')
                    continue
                # bruh this continue is needed or else the next if statement overflows if it is the last index lmao xd
                if line[charIdx+1] != '.':
                    print('occupied')
                    continue
                else: 
                    print(newlines[lineIdx][charIdx+1])
                    newlines[lineIdx][charIdx] = '.'
                    newlines[lineIdx][charIdx+1] = '>'
                    print(''.join(newlines[lineIdx]))


                continue

        

        # *** before var=newlines is called if char == 'v':
            # print('down m guy')

            # **FIRST CHECKED  CHECK IF PREVIOUS SEA PICKLE IS VALID TO MOVE AND REPLACE THE CURRENT INDEX WITH A PICKLEEEEEE, CONTINUE CURRENT ITERATION BECAUSE CURRENT INDEX WILL ALWAYS BE EMPTY AS CHECKED IN PREVIOUS ITERATION
            # if last in the line: check the beg of line (of not occupied, wrap to beginning of line)
            # if the one in front is occupied, continue
            

    iteration += 1
    for lineIdx in range(len(oldlines)):
        print(''.join(oldlines[lineIdx]))
    print('\n')
    for lineIdx in range(len(oldlines)):
        print(''.join(newlines[lineIdx]))