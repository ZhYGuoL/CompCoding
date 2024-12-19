def part1():
    bits = (open("Day3Input").read().splitlines())
    
    gammaStr = ""
    epsilonStr = ""
    count = []
    gamma = []
    epsilon = []
    for bitIdx in range(len(bits[0])):
        count = []
        for singleLine in bits:
            count.append(list(singleLine)[bitIdx])
        gamma.append(str(int(count.count("1") > count.count("0") * 1)))
    for idx in range(len(gamma)):
        epsilon.append(str(int(int(gamma[idx]) != 1)))
    for ele in (range(len(gamma))): 
        gammaStr += gamma[ele]  
        epsilonStr += epsilon[ele]
    print(int(epsilonStr,2)*int(gammaStr,2))

part1()



    # gamma = list(nums[0])
    # epsilon = []
    # print(gamma)
    # for bit in range(len(nums[0])):
    #     print(bit)
    #     bits = [i[bit] for i in nums]
    #     gamma[bit] = str(int(bits.count("1") > bits.count("0") * 1))
    #     epsilon[bit] = str(int(gamma[bit] != True))
    # print(gamma)
    # print(epsilon)
    
    # for a in range(len(gamma)):

# ==============================

def part2():

    nums_oxy = [l.strip() for l in open("Day3Input")]
    nums_car = nums_oxy.copy()

    for bit in range(len(nums_oxy[0])):

        bits_oxy = [l[bit] for l in nums_oxy]   # bits_oxy = count the number of '1's and '0's

        if bits_oxy.count('1') >= bits_oxy.count('0'):
            nums_oxy = [l for l in nums_oxy if l[bit] == '1']   # l = a line of nums_oxy. If l[current index] == '1'
        else:
            nums_oxy = [l for l in nums_oxy if l[bit] == '0']
        print(nums_oxy)
    print(nums_oxy)

    for bit in range(len(nums_car[0])):

        bits_car = [l[bit] for l in nums_car]   # bits_car = count the number of '1's and '0's

        if bits_car.count('1') >= bits_car.count('0'):
            nums_car = [l for l in nums_car if l[bit] == '0']
        else:
            nums_car = [l for l in nums_car if l[bit] == '1']

    print(int(nums_oxy[0], 2) * int(nums_car[0], 2))   # binary(base 2) to int(base 10)
part2()