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


def is_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]


def find_palindromic_bases(n):
    palindromic_bases = []

    for base in range(2, 37):
        number_in_base = decimal_to_base(n, base)
        if is_palindrome(number_in_base):
            palindromic_bases.append(base)

    return palindromic_bases


def decimal_to_base(decimal_number, base_k):
    if decimal_number == 0:
        return "0"

    res = ""
    while decimal_number > 0:
        remainder = decimal_number % base_k
        res = digit_to_char(remainder) + res
        decimal_number //= base_k

    return res


def main():
    n = int(input().strip())

    palindromic_bases = find_palindromic_bases(n)

    if not palindromic_bases:
        print("none")
    elif len(palindromic_bases) == 1:
        print("unique")
        print(palindromic_bases[0], end=" ")
    else:
        print("multiple")
        print(*palindromic_bases)


if __name__ == "__main__":
    main()
