a, b, c, d = map(int, input().split())
prods = []

for i in range(a, b + 1):
    for j in range(c, d + 1):
        res = i * j
        if res not in prods:
            prods.append(res)

variants = len(prods)

print(variants)

# https://www.eolymp.com/uk/submissions/15406115 (50%)
