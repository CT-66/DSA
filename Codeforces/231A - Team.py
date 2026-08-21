n = int(input())

w = []

for _ in range(n):
    x = input()
    w.append(x)

solved = 0

for i in w:
    if i.count("1") >= 2:
        solved += 1

print(solved)
