import sys

n, m, r, c = [int(i) for i in sys.stdin.readline().split()]
if n > 2 and m > 2:
    print("union")
    print("radar")
    print("badge")
    print("anime")
elif r == 2 and c == 2:
    print("aa")
    print("aa")
elif (r == 2 and c == 1) or (r == 1 and c == 2):
    print("IMPOSSIBLE")
elif (r == 2 and c == 0):
    print("aa")
    print("bb")

elif (r == 0 and c == 2):
    print("ab")
    print("ab")

elif r and c:
    print("aa")
    print("ab")
elif (r == 1 and c == 0):
    print("ab")
    print("cc")
elif (r == 0 and c == 1):
    print("ca")
    print("cb")
else:
    print("ab")
    print("cd")