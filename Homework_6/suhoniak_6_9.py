n = input()
operators = set("*/-+%")
counter = 0

if "**" in n:
    counter += n.count("**")
    n = n.replace("**", " ")

if "//" in n:
    counter += n.count("//")
    n = n.replace("//", " ")

for i in n:
    if i in operators:
        counter += 1

print(counter)

# https://www.eolymp.com/uk/submissions/15409556
