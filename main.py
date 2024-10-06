
def main():
    path_to_file = "./books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        print(num_of_words(file_contents))


# my solution    
def num_of_words(book):
    words = book.split() # line below creates a list of words from the book    
    return len(words) # line below returns simple list number of elements

#bd solution
'''
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
'''
main()
