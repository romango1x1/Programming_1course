def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    else:
        return chr(ord('A') + digit - 10)


def char_to_digit(char):
    if char.isdigit():
        return int(char)
    else:
        return ord(char) - ord('A') + 10


def base_to_decimal(number_m, base_m):
    decimal_number = 0
    power = len(number_m) - 1

    for digit_char in number_m:
        digit = char_to_digit(digit_char)
        decimal_number += digit * (base_m ** power)
        power -= 1

    return decimal_number


def decimal_to_base(decimal_number, base_k):
    if decimal_number == 0:
        return "0"

    result = ""
    while decimal_number > 0:
        remainder = decimal_number % base_k
        result = digit_to_char(remainder) + result
        decimal_number //= base_k

    return result


def main():
    m, k = map(int, input().split())
    number_m = input().strip()

    decimal_number = base_to_decimal(number_m, m)
    result = decimal_to_base(decimal_number, k)

    print(result)


if __name__ == "__main__":
    main()

# https://www.eolymp.com/uk/submissions/15428481
