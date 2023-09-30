n = int(input())
num = 1

while n > 0:
    if num % 2 and num % 3 and num % 5:
        print(num, end=' ')
        n -= 1
    num += 1

print()

# https://www.eolymp.com/uk/submissions/14467341
