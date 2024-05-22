def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
  #  print(f"{num_words} words found in the document")
    alphabet_dic = num_of_char(book_path)
    chars_sorted_list = sort_num_of_char(alphabet_dic)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_of_char(book_path):
    alphabet_dic = {}
    text = get_book_text(book_path)
    lowered_text = text.lower()
    words = lowered_text.split()
    for word in words:
        for char in word:
            if char.isalpha():
             if char in alphabet_dic:
                alphabet_dic[char] += 1
             else:
                alphabet_dic[char] = 1
    return alphabet_dic
    

def sort_num_of_char(dic):
    char_list = []

    def sort_on(dic):
        return dic["num"]

    for char, count in dic.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list


main()