def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def reverse_number(num):
    return int(str(num)[::-1])


def find_lucky_prime(K):
    count = 0
    num = 1

    while True:
        if is_prime(num) and is_prime(reverse_number(num)) and num != reverse_number(num):
            count += 1
            if count == K:
                return num
        num += 1


K = int(input())

print(find_lucky_prime(K))

# https://www.eolymp.com/uk/submissions/15428480
