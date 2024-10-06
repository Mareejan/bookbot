
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

main()
