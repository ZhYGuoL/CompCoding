import timeit
start = timeit.default_timer()

allIn = open("Day8Input").read().splitlines()
c = 0
for line in allIn:
    
    key, ns = [[set(x) for x in part.split()] for part in line.split(' | ')]
    # print(key)
    # print(ns)
    nums = {}
    nums[1] = next(x for x in key if len(x) == 2)
    print(nums)
    key.remove(nums[1])
    nums[7] = next(x for x in key if len(x) == 3)
    key.remove(nums[7])
    nums[4] = next(x for x in key if len(x) == 4)
    key.remove(nums[4])
    nums[8] = next(x for x in key if len(x) == 7)
    key.remove(nums[8])
    nums[9] = next(x for x in key if len(x ^ (nums[7] | nums[4])) == 1)
    key.remove(nums[9])
    nums[0] = next(x for x in key if nums[1] < x and len(x) == 6)
    key.remove(nums[0])
    nums[6] = next(x for x in key if len(x) == 6)
    key.remove(nums[6])
    nums[3] = next(x for x in key if nums[1] < x and len(x) == 5)
    key.remove(nums[3])
    nums[5] = next(x for x in key if len(nums[9] - x) == 1)
    key.remove(nums[5])
    nums[2] = key.pop()
    c += int(''.join(str(next(k for k, v in nums.items() if n == v)) for n in ns))
print(c)

stop = timeit.default_timer()
print('Time: ', stop - start) 