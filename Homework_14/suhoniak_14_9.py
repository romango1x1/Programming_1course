def read_content_file(file_path):
    try:
        with open(file_path, "r") as content_file:
            files = content_file.read().splitlines()
        return files
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except IOError:
        print(f"Error: Unable to read file {file_path}.")
        return None


def read_numbers(file_path):
    try:
        with open(file_path, "r") as numbers_file:
            numbers = []

            for line in numbers_file:
                try:
                    line_numbers = [float(num) for num in line.replace(",", ".").split()]
                    numbers.extend(line_numbers)
                except ValueError:
                    print(f"Error: file {line.strip()} contains non-numeric data.")
                    return None
        return numbers

    except FileNotFoundError:
        print(f"Error: file {file_path} not found.")
        return None

    except IOError:
        print(f"Error: Unable to read file {file_path}.")
        return None


def main():
    content_file_path = "content.txt"
    files = read_content_file(content_file_path)

    if files is not None:
        total_sum = 0
        for file_name in files:
            numbers = read_numbers(file_name)
            if numbers is not None:
                total_sum += sum(numbers)

        print(f"Total sum: {total_sum}")

main()
