
def main():
    path_to_file = "./books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        print(f"There are {num_of_words(file_contents)} words in this text")
        print("These are the number of times each letter appears in the text:", num_of_chars(file_contents))
        


# my solution    
def num_of_words(book):
    words = book.split() # line below creates a list of words from the book    
    return len(words) # line below returns simple list number of elements


def num_of_chars(book):
    deekshn = {}
    for w in book:
        llw = w.lower() # convert to lowercase              
        if llw not in deekshn:
            deekshn[llw] = 1 #first instance
        else:
            deekshn[llw] += 1 #not a first instance
    return deekshn # return the dictionarz
    



#bd solution

# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     print(f"{num_words} words found in the document")


# def get_num_words(text):
#     words = text.split()
#     return len(words)


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()

# main()



# ####
# number of letters:

# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     chars_dict = get_chars_dict(text)
#     print(chars_dict)


# def get_num_words(text):
#     words = text.split()
#     return len(words)


# def get_chars_dict(text):
#     chars = {}
#     for c in text:
#         lowered = c.lower()
#         if lowered in chars:
#             chars[lowered] += 1
#         else:
#             chars[lowered] = 1
#     return chars


# def get_book_text(path):
#     with open(path) as f:
#         return f.read()


# main()

main()
