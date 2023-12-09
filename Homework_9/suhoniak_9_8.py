n = int(input())
arr = list(map(int, input().split()))

dif_mod_nums = set(abs(num) for num in arr)
res = len(dif_mod_nums)

print(res)

# https://www.eolymp.com/uk/submissions/15428517 (84%)
