import sys

from stats import get_num_words
from stats import get_num_characters
from stats import sort_dict

# retrieves file text
def get_book_text(file_path): 
    with open(file_path) as book:
        text = book.read()
        return(text)
    book.closed

def main():
    # Get system arguments
    args = sys.argv

    # Check if passed 2 arguments
    # Exits with code 1 if 2 arguments were not passed
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = args[1]

    # text from file
    text = get_book_text(book_path)

    # counts words in text
    num_words = get_num_words(text)

    # get character count dictionary 
    num_chars = get_num_characters(text)

    # makes alphabetical sorted list of dictionary
    sorted_char_list = sort_dict(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_char_list:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
# returns the "file location : word count : character count" as a string 


# calls main function
if __name__ == "__main__":
    main()