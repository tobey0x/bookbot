with open("books/frankenstein.txt") as f:
    file_contents = f.read()


def count_words():
    words = str(file_contents).split()
    print(len(words))

count_words()
