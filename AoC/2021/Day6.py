import timeit
start = timeit.default_timer()

lanternfish = [int(i) for i in (open('Day6Input').read().split("\n"))[0].split(',')]
pos = [0] * 9
for i in lanternfish:
    pos[i] += 1
day = 256
for _ in range(day):
    pos0 = pos[0]
    for i in range(0, 8): 
        pos[i] = pos[i+1]
    pos[6] += pos0
    pos[8] = pos0
print(sum(pos))

stop = timeit.default_timer()
print('Time: ', stop - start) 