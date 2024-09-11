def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = count_words(text)
    print(f"there are {num_words} in the Document")



def count_words(text): 
        words = text.split()
        return len(words)
        
def get_text(path):
    with open(path) as f: 
        return f.read()


main() 
