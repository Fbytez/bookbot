import sys
from stats import get_num_words, get_char_count, print_report, read_book

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    title = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {title}" )
    print("----------- Word Count ----------")
    s = read_book(title)
    get_num_words(s)
    d = get_char_count(s)
    
    print("--------- Character Count -------")
    print_report(d)
    print("============= END ===============")



main()
