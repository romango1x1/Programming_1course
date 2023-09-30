post_fact = int(input())
n = 1
pre_fact = 1

while pre_fact < post_fact:
    n += 1
    pre_fact *= n

if pre_fact == post_fact:
    print(n)

# https://www.eolymp.com/uk/submissions/14478934 (80%)
