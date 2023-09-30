n = int(input())
factorial = 1
digit_count = 0

for i in range(1, n + 1):
    factorial *= i

while factorial > 0:
    factorial //= 10
    digit_count += 1

print(digit_count)

# https://www.eolymp.com/uk/submissions/14478679 (80%)
