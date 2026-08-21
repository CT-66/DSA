n = int(input())

w = []

for _ in range(n):
    x = input()
    w.append(x)

res = []

for i in w:
    if len(i) <= 10:
        res.append(i)
    else:
        res.append(i[0] + str(len(i) - 2) + i[-1])


for r in res:
    print(r)
