import sys
from stats import count_words
from stats import count_characters
from stats import sort_char_counts

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_counts = count_characters(text)
    sorted_char_counts = sort_char_counts(char_counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_char_counts:
        print(f"{char}: {count}")
    print("============= END ===============")

main()
