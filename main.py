def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_word_count(text)
    letterz_count = character_count(text)
    print(f"{letterz_count} is the number of times each individual letter appears")
    print(f"{word_count} words were found in the document")

def character_count(text):
    words = "".join(text).lower()
    characters_count = {}
    for letter in words:
        if letter in characters_count:
            characters_count[letter] +=1
        else:
            characters_count[letter] = 1
    return characters_count



def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
