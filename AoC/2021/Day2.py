# inputFile = open('Day2Input', 'r')
# raw = inputFile.readlines()
# processed = []

# for i in range(len(raw)):
#     processed.append(raw[i].strip())
# hpos=0
# vpos=0
# print(processed)
# for a in range(len(processed)):
#     instr = processed[a].split()
#     print(instr)
#     instr[1] = int(instr[1])
#     if instr[0] == 'forward':
#         hpos+=instr[1]
#     elif instr[0] == 'up':
#         vpos-=instr[1]
#     else:
#         vpos+=instr[1]

# print(vpos*hpos)



inputFile = open('Day2Input', 'r')
raw = inputFile.readlines()
processed = []

for i in range(len(raw)):
    processed.append(raw[i].strip())
hpos=0
vpos=0
aim=0
print(processed)
for a in range(len(processed)):
    instr = processed[a].split()
    print(instr)
    instr[1] = int(instr[1])
    if instr[0] == 'forward':
        hpos+=instr[1]
        vpos+=aim*instr[1]
    elif instr[0] == 'up':
        aim-=instr[1]
    else:
        aim+=instr[1]
        

print(vpos*hpos)
