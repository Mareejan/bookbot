
def main():
    path_to_file = "./books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        print(f"There are {num_of_words(file_contents)} words in this text")
        print("These are the number of times each letter appears in the text:", num_of_chars(file_contents))
        
def num_of_words(book):
    words = book.split() # line below creates a list of words from the book    
    return len(words) # line below returns simple list number of elements

def num_of_chars(book):
    deekshn = {}
    for w in book:
        llw = w.lower() # convert to lowercase              
        if llw in deekshn:
            deekshn[llw] += 1 #not a first instance
        else:
            deekshn[llw] = 1 #first instance
            
    return deekshn # return the dictionary
    
main()
