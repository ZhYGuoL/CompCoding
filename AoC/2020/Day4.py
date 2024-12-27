inputFile = open('Day4Input', 'r')
raw = inputFile.readlines()

correct = 0

rawButStr = ""

for i in range(len(raw)):
    rawButStr += raw[i]

passports = rawButStr.split("\n\n")

# print(passports)

reqs = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]



for i in range(len(passports)):
    passportNoSpace = []
    passport = passports[i].split("\n")
    for a in range(len(passport)):
        passportNoSpace.append(passport[a].split())
    print(passportNoSpace)
    for n in range(len(passportNoSpace)):
        for x in range(len(passportNoSpace[n])):
            print(passportNoSpace[n][x].split(":")[0])   
        if passportNoSpace[n][x].split(":")[0] in reqs:
                print("noice")
        else:
            print("not noice")
            continue







# print(inputFile)



# for i in range(len(raw)):
#     stripped.append(raw[i].strip())