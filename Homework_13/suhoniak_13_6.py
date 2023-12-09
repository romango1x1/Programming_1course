def create_text_file(sequence, output_file):
    max_row_length = 40

    rows = [sequence[i:i + max_row_length] for i in range(0, len(sequence), max_row_length)]

    with open(output_file, 'w') as file:
        for row in rows:
            file.write(row + '\n')


sequence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
output_file = "13_6.txt"

create_text_file(sequence, output_file)
