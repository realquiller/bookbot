from stats import get_number_of_words, get_each_character_count, sort_char_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # This ends the program with an error status.

    text = get_book_text(sys.argv[1])
    print (f"Found {get_number_of_words(text)} total words")

    char_list = get_each_character_count(text)
    sorted_char_list = []
    sorted_char_list = sort_char_dictionary(char_list)
    
    
    for char in sorted_char_list:
        print (f"{char['character']}: {char['count']}")

   # print (sort_char_dictionary(char_list))

main()

