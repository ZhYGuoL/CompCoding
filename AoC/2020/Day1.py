# inputFile = open('Day1Input', 'r')
# raw = inputFile.readlines()
# nums = []
    
# def solution(raw):
#     for i in range(len(raw)):
#         nums.append(int(raw[i].strip()))

#     for num1 in range(len(nums)):
#         for num2 in range(num1+1, len(nums)):
#             if nums[num1]+nums[num2]==2020:
#                 return(nums[num1]*nums[num2])

# print(solution(raw))


# ==================================================


inputFile = open('Day1Input', 'r')
raw = inputFile.readlines()
nums = []
    
def solution(raw):
    for i in range(len(raw)):
        nums.append(int(raw[i].strip()))

    for num1 in range(len(nums)):
        for num2 in range(num1+1, len(nums)):
            for num3 in range(num2+1, len(nums)):
                if nums[num1]+nums[num2]+nums[num3]==2020:
                    return(nums[num1]*nums[num2]*nums[num3])

print(solution(raw))