
text = "books/frankenstein.txt"



def main():

    with open(text) as f:
        content = f.read()
        print(content)



def count_words(): 
    with open(text) as f:
        content = f.read()
        words = content.split()
        return len(words)
        



#main() 
count_words()