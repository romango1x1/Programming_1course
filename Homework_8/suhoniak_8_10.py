def permutations(numbers):
    res = []

    for i in range(len(numbers)):
        current_number = numbers[i]
        remaining_numbers = numbers[:i] + numbers[i+1:]
        for p in permutations(remaining_numbers):
            res.append([current_number] + p)

    if len(numbers) == 1:
        return [numbers]
    
    return res


def print_permutations(n):
    numbers = [str(i) for i in range(1, n+1)]
    permutations_list = permutations(numbers)

    for p in permutations_list:
        print(' '.join(p))


n = int(input())

print_permutations(n)
