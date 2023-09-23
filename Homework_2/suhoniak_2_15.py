a, b, c = [int(nvm) for nvm in input().split()]

discriminant = b ** 2 - 4 * a * c

x1 = (-b - discriminant ** 0.5) / (2 * a)
x2 = (-b + discriminant ** 0.5) / (2 * a)

if discriminant < 0:
    print("No roots")
elif discriminant == 0:
    x = -b / (2 * a)
    print(f"One root: {int(x)}")
elif x1 < x2:
    print(f"Two roots: {int(x1)} {int(x2)}")
else:
    print(f"Two roots: {int(x2)} {int(x1)}")

# https://www.eolymp.com/uk/submissions/14368646
