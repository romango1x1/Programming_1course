n = int(input())
new_number = 0
digit_position = 1

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        new_digit = digit + 1
    else:
        new_digit = digit - 1
    new_number += new_digit * digit_position

    n //= 10
    digit_position *= 10

print(new_number)

# https://www.eolymp.com/uk/submissions/14479245
