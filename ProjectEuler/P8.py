raw = ["73167176531330624919225119674426574742355349194934",
    "96983520312774506326239578318016984801869478851843",
    "85861560789112949495459501737958331952853208805511",
    "12540698747158523863050715693290963295227443043557",
    "66896648950445244523161731856403098711121722383113",
    "62229893423380308135336276614282806444486645238749",
    "30358907296290491560440772390713810515859307960866",
    "70172427121883998797908792274921901699720888093776",
    "65727333001053367881220235421809751254540594752243",
    "52584907711670556013604839586446706324415722155397",
    "53697817977846174064955149290862569321978468622482",
    "83972241375657056057490261407972968652414535100474",
    "82166370484403199890008895243450658541227588666881",
    "16427171479924442928230863465674813919123162824586",
    "17866458359124566529476545682848912883142607690042",
    "24219022671055626321111109370544217506941658960408",
    "07198403850962455444362981230987879927244284909188",
    "84580156166097919133875499200524063689912560717606",
    "05886116467109405077541002256983155200055935729725",
    "71636269561882670428252483600823257530420752963450"]


# greatest = 0
# cur = raw[0:13]





# raw = '12345678912312312312332131111'
# cur = raw[0:13]
# largestProd = cur





largestProd = 1
largestDigits = raw[0][0:13]

row = raw[0]
cur = 1
zeroCount = 0
for j, i in enumerate(row[0:13]):
    if not int(i):
        zeroCount = 12 - j
        cur = 1
    else:
        cur = cur * int(i)
# print(row[0:13])
# print(cur)
for idx, digit in enumerate(row[13:len(raw)]):
    # print(digit)
    # print(cur)
    if not int(digit):
        # print(digit)
        
        zeroCount = 13
        cur = 1

    elif zeroCount > 0:
        cur = int(digit) * cur
        zeroCount = zeroCount-1
    else:
        print(row)
        print(idx)
        print(digit)
        print(row[idx])
        print(cur)
        print(largestProd)
        print(largestDigits)
        print('--------------')
        if not int(row[idx]):
            cur = cur*int(digit)
        else:
            cur = cur/int(row[idx])*int(digit)
        if cur > largestProd:
            largestProd = cur
            largestDigits = row[idx:idx+13]
print(largestProd)
print(largestDigits)

# print(cur)

# test = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
# for i in range(len(test)-12):
#     print(test[i:i+13])
#     print(''.join(test[i:i+13]))