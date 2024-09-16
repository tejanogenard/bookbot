def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = count_words(text)
    num_chars = count_characters(text)

    print("")
    print(f"--- Begin report of {book_path} ---")
    print("")
    print(f"{num_words} words were found inside Document.")
    print(f"\n")

    for char in num_chars:
        print(f"The `{char}` character was found {num_chars[char]} times!")

    print("")
    print("--- End report ---")


def count_words(text): 
        words = text.split()
        return len(words)

def count_characters(text):
    lowered_text = text.lower()
    num_chars = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0,
    'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0,
    'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
    'y': 0, 'z': 0
}
    for char in lowered_text:
        if char in num_chars:
            num_chars[char] += 1
    return num_chars

def sort_characters(num_chars):
    char_list = list(num_chars.items())
    sorted_characters = sorted(char_list, key=lambda x: x[1], reverse=True)
    return sorted_characters

def get_text(path):
    with open(path) as f: 
        return f.read()


main() 
