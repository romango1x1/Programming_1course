k = int(input())
n = int(input())

n_decimal = 0
power = 0

while n > 0:
    digit = n % 10
    n_decimal += digit * (k ** power)
    n //= 10
    power += 1

print(n_decimal)

# https://www.eolymp.com/uk/submissions/14479607
