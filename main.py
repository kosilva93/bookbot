import sys
from stats import get_num_words, get_num_characters, sort_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):

    with open(filepath) as f:
        return f.read()
    

def main():
    file = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file)} total words")
    print("--------- Character Count -------")
    
    char_count = sort_dict(get_num_characters(file))
    for item in char_count:
        print(f"{item}: {char_count[item]}")

    print("============= END ===============")


main()
