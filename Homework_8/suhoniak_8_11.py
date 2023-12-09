def func1(n):
    while n % 10 == 0 and n != 0:
        n /= 10
    return int(n % 10)


def func2(p, q):
    res = 0
    for number in range(p, q + 1):
        res += func1(number)
    return res


while True:
    p, q = map(int, input().split())
    if p == -1 and q == -1:
        break
    else:
        print(func2(p, q))

# https://www.eolymp.com/uk/submissions/15428494 (40%)
    