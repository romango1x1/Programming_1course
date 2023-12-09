def solve_quadratic_equation(a, b, c):
    assert a != 0, "Coefficient 'a' can not be equal 0"

    discriminant = b ** 2 - (4 * a * c)

    assert discriminant >= 0, "Negative discriminant, no solutions"

    x1 = (-b + (discriminant ** 0.5)) / (2*a)
    x2 = (-b - (discriminant ** 0.5)) / (2*a)

    return x1, x2


a, b, c = [float(el) for el in input().split()]
res = solve_quadratic_equation(a, b, c)
print(res)
