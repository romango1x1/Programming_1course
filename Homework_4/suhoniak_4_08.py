n = int(input())

cubed = []
i = 1

while i**3 < n:
    cubed.append(i ** 3)
    i += 1

print(" ".join(map(str, cubed)))

# https://www.eolymp.com/uk/submissions/14618442
