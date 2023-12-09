def power(n):
    res = ''
    for i in str(bin(n))[3:]:
        if i == '0':
            res += 'S'
        elif i == '1':
            res += 'SX'
    return res


n = int(input())
print(power(n))

# https://www.eolymp.com/uk/submissions/15428486
