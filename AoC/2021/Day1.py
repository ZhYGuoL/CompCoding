# inputFile = open('Day1Input', 'r')
# raw = inputFile.readlines()

# curnum = 0
# prevnum = 0
# counter = 0

# for i in range(len(raw)):
#     curnum = int(raw[i])
#     if curnum>prevnum:
#         counter+=1
#     prevnum=curnum

# print(counter-1)


# ================================================


inputFile = open('Day1Input', 'r')
raw = inputFile.readlines()

curnum = 0
prevnum = 0
counter = 0

for i in range(2,len(raw)):
    curnum = int(raw[i])+int(raw[i-1])+int(raw[i-2])
    if curnum>prevnum:
        counter+=1
    prevnum=curnum   

print(counter-1)


# ================================================


# with open('Day1Input', 'r') as file:
#     puzzle_input = [int(i) for i in file.read().splitlines()]

# count = prev_sum = 0
# for idx, i in enumerate(puzzle_input):
#     if idx > 2:
#         sum = i + puzzle_input[idx - 1] + puzzle_input[idx - 2]
#         if sum > prev_sum:
#             count += 1
#         prev_sum = sum

# print(count)