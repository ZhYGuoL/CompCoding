data = open('Day1Input.txt', 'r').read().split('\n')

parsed = [line.split('   ') for line in data]

left = sorted(int(line[0]) for line in parsed)
right = sorted(int(line[1]) for line in parsed)

total = sum(abs(l-r) for l, r in zip(left, right))

print(total)