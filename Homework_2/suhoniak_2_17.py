c, C = map(int, input().split())
a, A = map(int, input().split())
b, B = map(int, input().split())

on_line = (a - b) * (A - C) - (A - B) * (a - c) == 0

if on_line:
    print("YES")
else:
    print("NO")

if on_line and (b - a) * (c - a) + (B - A) * (C - A) >= 0:
    print("YES")
else:
    print("NO")

if on_line and (a - c) * (b - c) + (A - C) * (B - C) <= 0:
    print("YES")
else:
    print("NO")

# https://www.eolymp.com/uk/submissions/14369323
