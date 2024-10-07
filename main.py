
def main():
    book_file_name = "frankenstein.txt"
    path_to_file = "./books/"
    filepath = path_to_file + book_file_name
    try:
        with open(filepath) as f:
            file_content = f.read()
            print(f"\n --- Begin report of books/{book_file_name} ---")
            print(f"{num_of_words(file_content)} Words found in the document \n")
            sort_print_result(file_content)
            print(" ---  End report ---")
    except:
        print("Please Check the code !")

def num_of_words(text):
    words = text.split()
    return len(words)

def charz_count_dict(text):
    deekht = {}
    for ch in text:
        chs = ch.lower()
        if chs in deekht:
            deekht[chs] += 1
        else:
            deekht[chs] = 1
    return deekht

def sort_print_result(book):
    dict = charz_count_dict(book)
    tapl = list(dict.items())
    zorded = sorted(tapl, reverse=True, key=lambda shar: shar[1])
    for letter, count in zorded:
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")

    
main()
