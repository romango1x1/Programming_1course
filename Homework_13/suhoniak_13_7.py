def longest_word(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        words = file.read().split()
        longest_word = max(words, key=len)
        return longest_word


def count_words(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        words = file.read().split()
        return len(words)


def cleaning_list(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    words = content.split()
    cleaned_words = [word for word in words if len(word) > 1]
    cleaned_content = " ".join(cleaned_words)
    with open("H.txt", "w", encoding="utf-8") as output_file:
        output_file.write(cleaned_content)


file_path = "13_7.txt"
cleaning_list(file_path)
print(f"Longest word: {longest_word(file_path)}")
print(f"Amount of words: {count_words(file_path)}")

