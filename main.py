def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_word_count(text)
    letterz_count = character_count(text)
    report_details = report(letterz_count)
    print("--- Begin report of books/frankenstein.txt ---")
    
    print(f"{word_count} words were found in the document\n")

    print_number_of_times(report_details)

    print("--- End report ---")

def character_count(text):
    words = "".join(text).lower()
    characters_count = {}
    for letter in words:
        if letter in characters_count:
            characters_count[letter] +=1
        else:
            characters_count[letter] = 1
    return characters_count

def sort_on(dict):
    return dict["count"]

def report(letterz_count):
    letter_count = letterz_count
    list_of_dict = [{'letter':k, 'count': v} for k, v in letter_count.items()]
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

def print_number_of_times(report):
    letter_dict = report

    for i in letter_dict:
        if i["letter"].isalpha():
            print(f"The '{i['letter']}' character was found {i['count']} times")

def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
