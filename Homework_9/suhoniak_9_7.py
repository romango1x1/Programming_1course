n = int(input())
a = input()

if n % 2 == 0:
    print('Ok')

for i in a:
    if a.count(i) % 2:
        print(i)
        break

# https://www.eolymp.com/uk/submissions/15428512 (95%)