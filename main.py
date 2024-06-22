def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_word_count(text)
    print(f"{word_count} words were found in the document")

def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
