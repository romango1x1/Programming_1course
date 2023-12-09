def main():
    runtime_error_count = 0
    type_error_count = 0
    value_error_count = 0

    while True:
        try:
            user_input = input("Введіть число: ")

            if user_input.lower() == 'досить':
                break

            number = int(user_input)

            if number > 9:
                raise RuntimeError("Введене число більше 9")

            if number < 0:
                raise TypeError("Введене число менше 0")

            if 0 <= number <= 9:
                raise ValueError("Введене число в діапазоні від 0 до 9")

        except RuntimeError as e:
            print(f"Помилка: {e}")
            runtime_error_count += 1
        except TypeError as e:
            print(f"Помилка: {e}")
            type_error_count += 1
        except ValueError as e:
            print(f"Помилка: {e}")
            value_error_count += 1

    print(f"Кількість RuntimeError: {runtime_error_count}")
    print(f"Кількість TypeError: {type_error_count}")
    print(f"Кількість ValueError: {value_error_count}")


main()
