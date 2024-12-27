# def bubbleSort(arr):
#     n = len(arr)

#     for i in range(n-1):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
# arr = [64, 34, 25, 12, 22, 11, 90]
# bubbleSort(arr)

# print ("Sorted array is:")
# for i in range(len(arr)):
#     print ("% d" % arr[i])


# =====================================================================

# def arithmetic_operation(n):
# 	equa=n.split()
# 	if equa[1]=='+':
# 		return(int(equa[0])+int(equa[2]))
# 	elif equa[1]=='-':
# 		return(int(equa[0])-int(equa[2]))
# 	elif equa[1]=='*':
# 		return(int(equa[0])*int(equa[2]))
# 	elif equa[1]=='//':
# 		return(int(equa[0])/int(equa[2]))

# print(arithmetic_operation('12 // 12'))


# ======================================================================

# def is_economical(n):
# 	divisors = {}
# 	for div in range(1,n+1):
# 		if n / div == n // div:
# 			if div in divisors:
# 				divisors[div] += 1
# 			else:
# 				divisors[div] = 1

# 	# Get 'length' of divisors
# 	div_len = 0
# 	for (div, rep) in divisors.items():
# 		if rep != 1: div_len += len(str(rep))
# 		div_len += len(str(div))

# 	num_len = len(str(n))

# 	if div_len == num_len:
# 		return "Equidigital"
# 	elif div_len < num_len:
# 		return "Frugal"
# 	else:
# 		return "Wasteful"

# print(is_economical(14))


# =====================================================================
# Simple calculator

# def calculator(num1, operator, num2):
# 	if operator=='+':
# 		return num1+num2
# 	elif operator=='-':
# 		return num1-num2
# 	elif operator=='*':
# 		return num1*num2
# 	elif operator=='//':
# 		return num1/num2

# print(calculator(12, "*", 12))


# =====================================================================

# for i in range(len(str(x)))[::-1]:


# =====================================================================
# Reverse the list

# def reverse(self, x: int) -> int:
# 	revs_number = 0
# 	while (x > 0):
# 		remainder = x % 10
# 		revs_number = (revs_number * 10) + remainder
# 		x = x // 10
# 	return(revs_number)


# reverse(123879)


# =======================================================================
# Reverse list (keeps "+" or "-")

# class Solution:
#     def reverse(self, x):
#         neg=False
#         if x<0:
#             x=abs(x)
#             neg=True

#         revs_number=0
#         while (x>0):
#             remainder=x%10
#             revs_number=(revs_number*10)+remainder
#             x = x//10
#         if revs_number > 2**31-1:
#             return 0
#         elif neg:
#             return(-abs(revs_number))
#         else:
#             return(revs_number)


# ======================================================================
# Sort two (or more) lists

# def sortTwo(a, b):
# 	both = a
# 	for i in range(len(b)):
# 		both.append(b[i])
# 	both.sort()
# 	return(both)

# list1 = [4, 2, 6, 7]
# list2 = [2, 5, 7, 3]

# print(sortTwo(list1, list2))


# =======================================================================
# Median of list with library

# from statistics import median
# def Median(a):
# 	return(median(a))

# list = [1, 5, 2, 6, 8, 9]
# # [1, 2, 5, 6, 8, 9]
# print(Median(list))


# ========================================================================
# Sort  Median of list Without Library

# def Median(nums):
# 	n = len(nums)
# 	nums.sort()
# 	if n % 2 == 0:
# 		return((nums[n//2] + nums[n//2 - 1])/2)
# 	else:
# 		return(nums[n//2])

# print(Median([2,5,7,21,4,64]))  #2,4,5,7,21,64


# ========================================================================
# Mean of list (no library)

# def mean(nums):
# 	return(sum(nums) / len(nums))

# print(mean([1,6,3,7,9]))


# =========================================================================
# Sort Two (Or More) Lists And Find Median          DONE
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# def sortMedian(nums1, nums2):
# 	both = sorted(nums1+nums2)
# 	n = len(both)//2
# 	return[lambda: both[n],lambda:((both[n] + both[n - 1])/2)][len(both)%2==0]()


# =========================================================================
# Create List From Input then Sort          DONE
# https://dmoj.ca/problem/a4b1

# lenList = int(input())
# nums = []
# for i in range(lenList):
#     nums.append(int(input()))

# nums.sort()

# for a in range(lenList):
#     print(nums[a])


#============================================================================
# Evaluate Cubes of Inputs (With Multiple Test Cases)       DONE
# https://dmoj.ca/problem/a3

# def findNum(k):
#     increment=0
#     while(True):
#         if (((k+increment)**3) % 1000 == 888):
#             return(k+increment)
#         increment+=1


# TC=int(input())

# for i in range(TC):
#     k=int(input())
#     print(findNum(k))


# ===========================================================================
#PENDING PENDING PENDING
# Turn Decimal Into Binary and Add Spaces Every 4 Digits
# https://dmoj.ca/problem/binary

# a = list(bin(int(input())))
# binaryList = []
# a.remove("b")
# a.pop(len(a)-1)

# for i in range(len(a)):
#     if ((i+1) % 4 == 0):
#         binaryList.insert(0, a[i])
#         binaryList.insert(0, " ")
#         continue
#     binaryList.insert(0, a[i])

# if binaryList[0] == " ":
#     binaryList.pop(0)

# print("".join(binaryList))



# a = a = list(bin(int(input())))
# a.remove("b")
# a.pop(len(a)-1)
# print(a)


# ============================================================================
# PENDING PENDING PENDING
# Divide List By Specified Keyword/s


# import re
# def sepValue (n, *keys):
#     for i in range(len(keys)):
#         n = re.split(keys[i])

#     return(n[12])


# str1 = "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked. Only the Avatar, master of all four elements, could stop them, but when the world needed him most, he vanished. A hundred years passed, and my brother and I discovered the new Avatar, an airbender named Aang. And although his airbending skills are great, he has a lot to learn before he's ready to save anyone. But I believe Aang can save the world."
# print(sepValue(str1, " ", ". ", ", "))


# str1 = ["123", "abc", "def"]
# print(str1[2][2])

#===============================================================================
# Find The Biggest Palendrome In a String       DONE
# https://dmoj.ca/problem/ccc16j3

# word = input()
# biggest = 0
# for i in range(len(word)+1):
#     for n in range(len(word)+1):
#         curWord=word[i:n]
#         if word[::-1]:
#             if len(curWord)>biggest:
#                 biggest = len(curWord)

# print(biggest)


# ===============================================================================


# begin, end = int(input()), int(input())       Pending
# counter = 0

# for i in range(begin, end+1):     #every num between and including begin, end
#     for n in range(len(str(i))):    #len of num to check every char
#         if (str(i)[n]==2 or str(i)[n]==3 or str(i)[n]==4 or str(i)[n]==5 or str(i)[n]==7):
#             continue

# print(counter)


# ================================================================================
# CCC S2 Multiple choice            DONE
# https://dmoj.ca/problem/ccc11s2


# choices = int(input())
# a = []
# b = []
# d = 0
# for i in range(choices):
#     c = str(input())
#     a.append(c)
# for i in range(choices):
#     c = str(input())
#     b.append(c)

# for  i in range(choices):
#     if a[i].eq(b[i]):
#         d+=1
# print(d)


# ===============================================================================
# LeetCode 5. Longest Palindromic Substring          IN PROGRESS
#https://leetcode.com/problems/longest-palindromic-substring/


# def solution(s):
#     for i in s:



# def findPalindrone(str):


#================================================================================
# DMOJ CCC 2000 J2 - Inverted numbers that are the same         DONE
# https://dmoj.ca/problem/ccc00j2


# from math import ceil

# low = int(input())
# high = int(input())+1

# def valid(num):
#     for i in num:
#         if i in ['2', '3', '4', '5', '7']:
#             return False
#     return True

# def checkIfSame(num, newNum):
#     for i in range(ceil(len(num)/2)):
#         if num[i] == newNum[len(num)-i-1]:
#             continue
#         return False
#     return True

# counter = 0

# for num in range(low, high):
#     num = [str(x) for x in str(num)]
#     if valid(num) == False:
#         continue

#     newNum = num.copy()

#     for x in range(len(num)):
#         if num[x] == '6':
#             newNum[x] = '9'
#         elif num[x] == '9':
#             newNum[x] = '6'

#     if checkIfSame(num, newNum):
#         counter+=1
# print (counter)


# ==============================================================================
# DM:OJ Mispelling      PENDING
# https://dmoj.ca/problem/a1


# for x in range(int(input())):
#     word = []
#     line = input().split(' ')
#     for i in range(len(line[1:len(line)])):
#         word += [x for x in line[i]]
#         print(word)
#     word.pop(int(line[0])-1)
#     print(int(x)+1, ''.join(word))


#================================================================================
# DMOJ CCC '21 S2 Modern Art                DONE
# https://dmoj.ca/problem/ccc21s2


# k = lambda:int(input())
# height = k()
# width = k()

# Rlines = {}
# Clines = {}

# for i in range(k()):
#     line, pos = input().split(' ')
#     if line == 'R':
#         if pos in Rlines:
#             del Rlines[pos]
#         else:
#             Rlines[pos] = 0

#     else:
#         if pos in Clines:
#             del Clines[pos]
#         else:
#             Clines[pos] = 0

# # print(len(Rlines), len(Clines))

# print(len(Rlines)*(width-len(Clines))+len(Clines)*(height-len(Rlines)))


#==================================================================================
# Whatever the fuck this is      PENDING


# xSquared, sign1, x, sign2, constant = input().split(' ')
# xSquared = xSquared[2:]
# print(xSquared, sign1, x, sign2, constant)
# print()


#===================================================================================
# DMOJ CCC 2015 J3      DONE
# https://dmoj.ca/problem/ccc15j3


# newWord = ''
# vowels = {'a', 'e', 'i', 'o', 'u'}
# word = input()
# for char in word:

#     if char in vowels:
#         newWord += char
#         continue

#     newWord += char
#     unicode = ord(char)

#     closestVowel = min(abs(97-unicode), abs(101-unicode), abs(105-unicode), abs(111-unicode), abs(117-unicode))

#     if chr(unicode-closestVowel) in vowels:
#         newWord += chr(unicode-closestVowel)

#     else:
#         newWord += chr(unicode+closestVowel)

#     if char == 'z':
#         newWord += 'z'
#     elif chr(unicode+1) in vowels:
#         newWord += chr(unicode+2)
#     else:
#         newWord += chr(unicode+1)


# print(newWord)


# =================================================================================
# DMOJ AAC 5 P2            DONE
# https://dmoj.ca/problem/aac5p2


# from math import sqrt
# from math import gcd

# numbersArranged = ''

# N = int(input())

# if N == 3:
#     print('? 1 2')
#     zeroxOne = int(input())

#     print('? 1 3')
#     zeroxTwo = int(input())

#     num1 = int(gcd(zeroxOne, zeroxTwo))

#     numbersArranged = str(num1) + ' ' + str(int(zeroxOne/num1)) + ' ' + str(int(zeroxTwo/num1))

#     a = num1 + zeroxOne/num1

#     print('! '+ numbersArranged)

# else:

#     print('? 1 2')
#     zeroxOne = int(input())

#     print('? 1 3')
#     zeroxTwo = int(input())

#     print('? 2 3')
#     onexTwo = int(input())

#     num1 = int(sqrt(zeroxOne*zeroxTwo/onexTwo))
#     num2 = int(zeroxOne/num1)
#     num3 = int(onexTwo/(zeroxOne/num1))
#     allNumbersCombined = num1 + num2 + num3
#     prevNum = num3
#     numbersArranged = str(num1) + ' ' + str(num2) + ' ' + str(num3) + ' '

#     for curNum in range(4, N):
#         print('? ' + str(curNum-1) + ' ' + str(curNum))

#         prevNum = int(int(input())/prevNum)

#         numbersArranged += str(prevNum) + ' '

#         allNumbersCombined += prevNum

#     a = 0
#     for i in range(N+1):
#         a += i

#     print('! '+ numbersArranged + str(int(a-allNumbersCombined)))


# ================================================================================
# DMOJ '13 J4 - Time on Task        DONE
# https://dmoj.ca/problem/ccc13j4


# time = int(input())

# times = []
# x = int(input())

# for i in range(x):

#     times.append(int(input()))

# times.sort()
# counter = 0
# for i in range(x):
#     if time - times[i]>=0:
#         counter+=1
#         time-=times[i]
#     else:
#         break
# print(counter)


# ====


# from sys import setrecursionlimit

# setrecursionlimit(69696969)


# n = int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]

# dis = [[-1] * (n + 1) for _ in range(n + 1)]


# def dfs(i, j):
#     if dis[i][j] != -1:
#         return dis[i][j]

#     dis[i][j] = 0
#     if i < n - 1 and grid[i + 1][j] < grid[i][j]:
#         dis[i][j] = dfs(i + 1, j) + 1
#     if i > 0 and grid[i - 1][j] < grid[i][j]:
#         dis[i][j] = max(dis[i][j], dfs(i - 1, j) + 1)
#     if j < n - 1 and grid[i][j + 1] < grid[i][j]:
#         dis[i][j] = max(dis[i][j], dfs(i, j + 1) + 1)
#     if j > 0 and grid[i][j - 1] < grid[i][j]:
#         dis[i][j] = max(dis[i][j], dfs(i, j - 1) + 1)

#     return dis[i][j]

# best = -1
# for i in range(n):
#     for j in range(n):
#         best = max(best, dfs(i, j))
# print(best)


# ===================================================================
# *BFS* https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python

# graph = {
#   'A' : ['B','C'],
#   'B' : ['D', 'E'],
#   'C' : ['F'],
#   'D' : [],
#   'E' : ['F'],
#   'F' : []
# }

# visited = [] # List to keep track of visited nodes.
# queue = []     #Initialize a queue

# def bfs(visited, graph, node):
#   visited.append(node)
#   queue.append(node)

#   while queue:
#     s = queue.pop(0)
#     print (s, end = " ")

#     for neighbour in graph[s]:
#       if neighbour not in visited:
#         visited.append(neighbour)
#         queue.append(neighbour)

# # Driver Code
# bfs(visited, graph, 'A')


# =========================================================================
# *DFS* https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python


# # Using a Python dictionary to act as an adjacency list
# graph = {
#     'A' : ['B','C'],
#     'B' : ['D', 'E'],
#     'C' : ['F'],
#     'D' : [],
#     'E' : ['F'],
#     'F' : []
# }

# visited = set() # Set to keep track of visited nodes.

# def dfs(visited, graph, node):
#     if node not in visited:
#         print (node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)

# # Driver Code
# dfs(visited, graph, 'A')







# numItems, limit = [int(x) for x in sys.stdin.readline().strip('\n').split()]
# items = []

# for _ in range(numItems):
#     items.append(input().split())

# sorted(items, lambda x: x[1]/x[0])

# curCap = 0
# curPoints = 0

# for _ in range(len(items)):
#     if items[0] + counter <= limit:



# =========================================================================================
# Simple Pi

# # Initialize denominator
# k = 1

# # Initialize sum
# s = 0

# for i in range(1000000):

#     # even index elements are positive
#     if i % 2 == 0:
#         s += 4/k
#     else:

#         # odd index elements are negative
#         s -= 4/k

#     # denominator is odd
#     k += 2

# print(s)


# =========================================================================================
# Mock CCC '14 S3
# https://dmoj.ca/problem/mockccc14s3
# sort lists through one index of each list

# height, width = map(int, input().split())

# spreadsheet = []

# for i in range(height):
#     spreadsheet.append(list(map(int, input().split())))

# for _ in range(int(input())):
#     a = int(input())
#     spreadsheet = sorted(spreadsheet, key=lambda x: x[a-1])


# # print spreadsheet
# for i in range(height):
#     print(*spreadsheet[i])

