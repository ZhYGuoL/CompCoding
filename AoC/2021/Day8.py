import difflib

raw = open("Day8Input").read().split('\n')
inputStrings = []
for i in range(len(raw)):
    inputStrings.append(raw[i].split(' | ')[1])
    inputDecipher.append(raw[i].split(' | ')[0])

counter = 0


# for num in inputStrings:
#     indNum = num.split(' ')
#     for chars in indNum:
#         print(chars)
#         if len(chars) == 2:
#             
#         if len(chars) == 4:
#             counter+=1
#             continue
#         if len(chars) == 3:
#             counter+=1
#             continue
#         if len(chars) == 7:
#             counter+=1
#             continue

pos = [''] * 9
nums = []

for num in inputStrings:
    indNum = num.split(' ')
    for idx, chars in enumerate(indNum):
        print(chars)
        if len(chars) == 2:
            if 
            
        if 


# make list of nums corresponding to the indexes of teh string list
# not possible will be None
# 

        if len(chars) == 4:
            counter+=1
            continue
        if len(chars) == 3:
            counter+=1
            continue
        if len(chars) == 7:
            counter+=1
            continue
print(counter)

print(inputStrings)