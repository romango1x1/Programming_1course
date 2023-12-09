def to_base13(n):
    if n == 0:
        return "0"

    res = ""

    while n > 0:
        remainder = n % 13
        if remainder < 10:
            res = str(remainder) + res
        else:
            res = chr(ord("A") + remainder - 10) + res
        n = n // 13

    return res


n = int(input())

print(to_base13(n))

# https://www.eolymp.com/uk/submissions/15428487
