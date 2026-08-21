n = int(input())

t = sorted("Timur")

res = ""

for i in range(n):
    n = int(input())
    w = input()
    w = sorted(w)
    if w == t:
        res += "YES\n"
    else:
        res += "NO\n"


print(res)


