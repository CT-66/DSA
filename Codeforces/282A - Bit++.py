n = int(input())

res = 0

for _ in range(n):
    x = input()
    if "--" in x:
        res -= 1
    elif "++" in x:
        res += 1

print(res)
