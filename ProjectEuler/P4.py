def isPalindrome(strNum):
    for idx in range(int(len(strNum)/2)):
        if strNum[idx] != strNum[len(strNum)-idx-1]:
            return False
    return True

largest = 0

for i in range(999, 1, -1):
    for j in range(999, i, -1):
        if isPalindrome(str(i*j)):
            largest = max(largest, i*j)
            break
print(largest)