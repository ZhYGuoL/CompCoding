inputFile = open('Day2Input', 'r')
raw = inputFile.readlines()
stripped = []

for i in range(len(raw)):
    stripped.append(raw[i].strip())

correct = 0


# for tc in range(len(stripped)):
#     counter = 0
#     requirement = (stripped[tc].split())[0]
#     minreq = int((requirement.split("-"))[0])
#     maxreq = int((requirement.split("-"))[1])
#     kword = (stripped[tc].split())[1][0]
#     password = (stripped[tc].split())[2]

#     for char in (range(len(password))):
#         if kword == password[char]:
#             counter+=1

#     if (counter <= maxreq and counter >= minreq):
#         correct+=1

#  print(correct)


# ====================================================


for tc in range(len(stripped)):
    counter = 0
    requirement = (stripped[tc].split())[0]
    num1 = int((requirement.split("-"))[0])-1
    num2 = int((requirement.split("-"))[1])-1
    kword = (stripped[tc].split())[1][0]
    password = (stripped[tc].split())[2]

    if ((password[num1] == kword and password[num2] != kword) or (password[num1] != kword and password[num2] == kword)):
        correct+=1


print(correct)