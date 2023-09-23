x, y, x1, y1, x2, y2 = map(float, input().split())

min_x = min(x1, x2)
max_x = max(x1, x2)
min_y = min(y1, y2)
max_y = max(y1, y2)

if min_x <= x <= max_x and min_y <= y <= max_y:
    print(1)
else:
    print(0)

# https://www.eolymp.com/uk/submissions/14308988
