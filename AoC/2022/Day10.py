data = open("Day10Input.txt").read().splitlines()
res = 0
st = [1]
sprite = 0
for x in data:
    k = x.split()
    if len(k) > 1:
        st.append(0)
        st.append(int(k[1]) )
    else:
        st.append(0)

for x in [20, 60, 100, 140, 180, 220]:
    res += sum(st[:x]) * x
print(res)

res = [str() for _ in range(6)]

for i in range(0, 240, 40):
    for j in range(40):
        sprite += st[i + j] if i + j < len(st) else 0
        res[i // 40] += ['.', '#'][j in range(sprite - 1, sprite + 2)]

for x in res:
    print(x)

