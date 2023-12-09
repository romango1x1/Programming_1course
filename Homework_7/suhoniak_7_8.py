def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def count_pairs(a, b):
    count = 0

    for i in range(1, b + 1):
        if (a * b) % i == 0:
            if gcd((a * b) // i, i) == a and lcm((a * b) // i, i) == b:
                count += 1

    return count


a, b = map(int, input().split())

print(count_pairs(a, b))

# https://www.eolymp.com/uk/submissions/15428437
