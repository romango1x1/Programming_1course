x, y = [float(nvm) for nvm in input().split()]
a = (2 * x * y) / ((x ** 2 + y ** 2) ** 0.5)
b = ((x + y - 1) ** 2) / (x * y)
c = a - b

print(round(c, 3))

# https://www.eolymp.com/uk/submissions/14225622
