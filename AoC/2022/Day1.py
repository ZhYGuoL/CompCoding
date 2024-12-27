raw = open('Day1Input.txt').readlines()
biggestElf = 0
currentElf = 0

for i in range(len(raw)):
    if raw[i] == "\n":
        if biggestElf < currentElf:
            biggestElf = currentElf
            currentElf = 0
    else:
        currentElf += int(raw[i])

print(biggestElf)

# with open("Day1Input.txt") as f:
#     content = f.readlines()

# elves = [0]
# current_elf = 0
# for v1 in content:
#     if v1.strip() == "":
#         current_elf += 1
#         elves.append(0)
#     else:
#         elves[current_elf] += int(v1.strip())

# print(elves)
# print(max(elves))
# elves.sort(reverse=True)
# print(elves[0] + elves[1] + elves[2])



# from aoc_tools import *

with open("Day1Input.txt") as f:
    s = f.read()

s = s.strip().split("\n\n")

s = [[int(x) for x in y.split("\n")] for y in s]

print(max(sum(z) for z in s))

s.sort(key = lambda x : sum(x), reverse=True)

print(sum(sum(z) for z in s[:3]))