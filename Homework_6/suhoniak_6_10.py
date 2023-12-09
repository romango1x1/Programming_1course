n = input().strip()
output = ""

for i in n:
    if i.isalpha():
        output += i * 2
    else:
        output += i

print(output)

# https://www.eolymp.com/uk/submissions/15409577
