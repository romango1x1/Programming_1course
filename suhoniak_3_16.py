M = int(input())
x = 0

for i in range(M, 0, -1):
    square = i * i
    num_digits = len(str(i))

    if square % (10 ** num_digits) == i:
        x = i
        break

print(x)

# https://www.eolymp.com/uk/submissions/14478803 70%
