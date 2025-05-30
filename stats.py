test_text = list("Meow meow meow. The quick brown fox jumps over the lazy dog.")


def count_words(file_text):
    word_count = len(file_text.split())
    return word_count


def count_letters(file_text):
    letter_count = {}
    {letter: 1
            if letter.lower() not in letter_count and not letter_count.update({letter.lower(): 1})
                else letter_count[letter.lower()] + 1
            if not letter_count.update({letter.lower(): letter_count[letter.lower()] + 1})
                else 1
        for letter in file_text}
    return letter_count


def sort_letters(letter_dictionary):
    sorted_letter_dictionary = {letter: count for letter, count in sorted(letter_dictionary.items(), reverse=True, key=lambda item: item[1])}
    return sorted_letter_dictionary


if __name__ == "__main__":
    print(count_letters(test_text))
    print(sort_letters(count_letters(test_text)))


