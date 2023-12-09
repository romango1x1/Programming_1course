def count_elements(lst):
    if not lst:
        return 0
    return 1 + count_elements(lst[1:])


def sum_elements(lst):
    if not lst:
        return 0
    return lst[0] + sum_elements(lst[1:])


def max_ratio(lst):
    if len(lst) < 2:
        return None
    max_val = max(lst)
    min_val = min(lst)
    if min_val == 0:
        return float('Can not divide by zero')
    return max_val / min_val


numbers = [10, 221, 35, 74, 88, 245, 62, 27, 400]

print(f"a) Amount of elements: {count_elements(numbers)}")
print(f"b) Sum of elements: {sum_elements(numbers)}")
print(f"c) Maximum ratio: {max_ratio(numbers)}")
