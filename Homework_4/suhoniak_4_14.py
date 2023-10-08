n = int(input())
max_divisor = 1

for i in range(2, n):
    if n % i == 0:
        max_divisor = i

print(max_divisor)

# https://www.eolymp.com/uk/submissions/14618345 (60%)
