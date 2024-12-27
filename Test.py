L = 'ABCDEFGHIJKLMNOPQRST'  # letters
N = '123456789'  # numbers
S = ''

t = input()
t = list(t)

for i in range(len(t)):
    if t[i] in L:
        if t[i - 1] in N:
            t.insert(i, '?')
t.pop(0)
# print(t)

for i in t:
    S += i

S = S.replace('+', ' tighten ')
S = S.replace('-', ' loosen ')
S = S.replace('?', '\n')

print(S)

