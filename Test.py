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

<<<<<<< HEAD
S = S.replace('+', ' tighten ')
S = S.replace('-', ' loosen ')
S = S.replace('?', '\n')

print(S)
=======
wordgenerator = input().lower()
print(palindromecreator(wordgenerator))
>>>>>>> 5e0346e1acef0d658655888ca5c68f3c6ef71e63

<<<<<<< HEAD
=======


>>>>>>> 4ee88b59feed55f814ad0d6050fa3c3013b0922e
