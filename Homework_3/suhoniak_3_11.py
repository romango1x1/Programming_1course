n = int(input())
even_sum = 0
while n > 0:
    number = n % 10
    if number % 2 == 0:
        even_sum += number
    n //= 10

if even_sum > 0:
    print(even_sum)
else:
    print(-1)

# https://www.eolymp.com/uk/submissions/14479340 (90%)
