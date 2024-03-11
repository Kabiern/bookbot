def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dict = get_dict(text)
    sorted_list = sort_dict(dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for c in sorted_list:
        if not c["char"].isalpha():
            continue
        print(f"The '{c['char']}' character was found {c['num']} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_dict(text):
    characters = {}
    for letter in text:
        if letter.lower() in characters:
            characters[letter.lower()] += 1
        else:
            characters[letter.lower()] = 1
    return characters

def sort_on(dict):
    return dict["num"]
    
def sort_dict(dictionary):
    lst = []
    for c in dictionary:
        lst.append({"char": c, "num": dictionary[c]})
    lst.sort(reverse=True, key=sort_on)
    return lst

main()