import sys

from stats import get_num_words
from stats import get_character_count
from stats import sort_char_count

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    frankenstein_text = get_book_text(book_path)
    num_words = get_num_words(frankenstein_text)
    char_count = get_character_count(frankenstein_text)
    splited = sort_char_count(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in splited:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")




main()
