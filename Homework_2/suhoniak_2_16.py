n = int(input())

if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
    print("YES")
else:
    print("NO")

# https://www.eolymp.com/uk/submissions/14368798
