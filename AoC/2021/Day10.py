lines = [line for line in open('Day10Input').read().strip().split('\n')]

pairs = {'[': ']', '{': '}', '<': '>', '(': ')'}

value = {']': 57, ')': 3, '}': 1197, '>': 25137}
starters = list(pairs.keys())

for (left, right) in list(pairs.items()):
    pairs[right] = left
points = 0
for line in lines:
    stack = []
    for char in line:

        if char in starters:
            stack = [char] + stack
        else:
            if not stack:
                continue
            expected = pairs[stack[0]]
            stack = stack[1:]
            
            if expected == char:
                continue
            points += value[char]
            break
print(points)



closeOpen = {')':'(', ']':'[', '}':'{', '>':'<'}
points = {'(':1, '[':2, '{':3, '<':4}
scores = []



for line in lines:
    stack = []

    for char in list(line):
        if char in closeOpen.values():
            stack.append(char)
        elif not stack or stack.pop() != closeOpen[char]:
            stack = None
            break

    print(stack)

    if stack:
        indScore = 0

        for char in stack[::-1]:
            indScore = 5 * indScore + points[char]

        scores.append(indScore)

print(sorted(scores)[len(scores) // 2])