def count_even_numbers(path):
    res = 0

    for el in path:
        if int(el) % 2 == 0:
            res += 1
    return res


def count_odd_numbers_squares(path):
    res = 0

    for el in path:
        if (int(el) ** 0.5) % 2 == 1:
            res += 1
    return res


def max_min_difference(path):
    return max(path) - min(path)


def longest_increasing_length(path):
    lengths = [1] * len(path)

    start_marker, end_marker = 0, len(path) - 1

    while start_marker < end_marker:
        for j in range(start_marker + 1, end_marker + 1):
            if path[j] > path[j - 1] and lengths[j] <= lengths[j - 1]:
                lengths[j] = lengths[j - 1] + 1

        for i in range(end_marker - 1, start_marker - 1, -1):
            if path[i] > path[i + 1] and lengths[i] <= lengths[i + 1]:
                lengths[i] = lengths[i + 1] + 1

        start_marker += 1
        end_marker -= 1

    max_length = max(lengths)

    return max_length


with open("13_5.txt", "r", encoding="utf-8") as file:
    content = file.read().split()
    numbers = [int(el) for el in content]

    print(f"a) amount of even numbers: {count_even_numbers(numbers)}")
    print(f"b) amount of squares of odd numbers: {count_odd_numbers_squares(numbers)}")
    print(f"c) difference between the largest even and the smallest odd number: {max_min_difference(numbers)}")
    print(f"d) length of the longest increasing sequences: {longest_increasing_length(numbers)}")
