# def solve(input_string, output_string):
#     c1_to_c2 = {}
#     for c1, c2 in zip(input_string, output_string):
#         if c1 in c1_to_c2 and c1_to_c2[c1] != c2:
#             return -1
#         c1_to_c2[c1] = c2
#     return len(c1_to_c2)

# t = int(input().strip())
# for _ in range(t):
#     input_string = input().strip()
#     output_string = input().strip()
#     print(solve(input_string, output_string))

# def main():
#     t = int(input().strip())
#     for i in range(t):
#         inStr = input().strip()
#         outStr = input().strip()
#         flag = True
#         d = {}
#         for j in range(len(inStr)):
#             if inStr[j] in d:
#                 if d[inStr[j]] != outStr[j]:
#                     flag = False
#                     break
#             else:
#                 if outStr[j] in d.values():
#                     flag = False
#                     break
#                 d[inStr[j]] = outStr[j]
#         if flag:
#             print(len(set(outStr)) - len(d))
#         else:
#             print(-1)

# if __name__ == "__main__":
#     main()



#T is the number of independent test cases
T = int(input())

#Loop through each case
for _ in range(T):
    #input_string and output_string are the strings given
    input_string = input()
    output_string = input()
    
    #Initialize keystrokes to 0
    keystrokes = 0
    
    #Loop through the length of the input string
    for i in range(len(input_string)):
        #If the characters at the same index in the two strings are not the same, increment keystrokes and break out of loop
        if input_string[i] != output_string[i]:
            keystrokes += 1
            break
    #If keystrokes is still 0, it means all the characters are the same and no keystrokes are needed
    if keystrokes == 0:
        print(keystrokes)
    #Else, check if the rest of the strings match, if they do not, then it is not possible and print -1
    else:
        if input_string[i+1:] != output_string[i+1:]:
            print(-1)
        #Else, print the number of keystrokes
        else:
            print(keystrokes)