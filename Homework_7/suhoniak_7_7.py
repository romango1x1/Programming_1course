def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def find_lcm(n):
    res = 1
    for i in range(1, n + 1):
        res = lcm(res, i)
    return res


n = int(input())

print(find_lcm(n))

# https://www.eolymp.com/uk/submissions/15428446
