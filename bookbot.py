

file = input(f"Type File Path: ")

with open(f"{file}") as f:
    file_contents = f.read()


def count_words(file):
    count = 0
    words = file.split()
    for word in words:
        count += 1
    return count


def count_letters(file):
    letter_count = {}
    lower_file = file.lower()
    words = lower_file.split()
    for word in words:
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    counted_phrase = []
    sorted_letter_count = sorted(letter_count.items(), key=lambda x:x[1], reverse=True)
    for key, value in sorted_letter_count:
        if key.isalpha() == True:
            counted_phrase.append(f"The '{key}' character was found '{value}' times.")
    return counted_phrase


def print_count_message(file):
    print(f"\n--- Being report of file. ---")
    print(f"{count_words(file)} words found in the document.\n")

    for i in count_letters(file):
        print(i)

    print(f"--- End Report ---")

print_count_message(file_contents)
