x = int(input())
y = 1
while x > 0:
    z = x % 10
    x = x // 10
    y *= z

print(y)

# https://www.eolymp.com/uk/submissions/14225021
