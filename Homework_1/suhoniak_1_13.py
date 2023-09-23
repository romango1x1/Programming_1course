x, y = [float(nvm) for nvm in input().split()]
a = ((x ** 2) - (2 * x * y) + 4 * (y ** 2)) / (x + 5)
b = (3 * (x ** 2) - (y ** 2)) / (y-7)
c = a + b

print(f"{c:.4}")

# https://www.eolymp.com/uk/submissions/14225554
