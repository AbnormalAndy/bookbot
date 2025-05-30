from stats import count_words, count_letters, sort_letters
import sys


#TXT_FILE_LOCATION = "books/frankenstein.txt"


def get_book_text(file_path):
    with open(f"{file_path}", mode="r") as book:
        book_text = book.read()
        return book_text


def main():
    args = sys.argv
    

    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        txt_file_location = args[1]
        book_contents = get_book_text(txt_file_location)
        book_word_count = count_words(book_contents)
        book_letter_count = count_letters(book_contents)
        book_letter_sorted = sort_letters(book_letter_count)


        print(f""""
        ============ BOOKBOT ============
        Analyzing book found at {txt_file_location}...
        ----------- Word Count ----------
        Found {book_word_count} total words
        --------- Character Count -------""")
        #print(book_letter_sorted)
        for letter, count in book_letter_sorted.items():
            if letter.isalpha():
                print(f"{letter}: {count}")
        print("============= END ===============")

    
main()


