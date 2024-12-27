import sys

num = int(sys.stdin.readline())
# valid = [x for x in range(num+1)]

# for i in range(num+1):
#     if i == 0:
#         print(0, end=" ")
#     elif i == num:
#         print(i, end=" ")
    
# def a(curRange):
#     valid.remove(curRange[int(len(curRange/2))])
#     if len(curRange) == 3:
#         return
#     else:

def baseThree(n):
    if n < 3:
        return n
    s = ''
    while n != 0:
        s = str(n%3) + s
        n = n//3
    return s

valid = []

for i in range(num+1):
    print(baseThree(i/num))
    print(i/num)
    if str(baseThree(i/num)).count('1') < 2:
        print(i)
