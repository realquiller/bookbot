def get_number_of_words(text):
    num_words = 0
    word_list = text.split()
    for i in range(0, len(word_list)):
        num_words += 1
    return num_words

def get_each_character_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def sort_char_dictionary(char_dict):
    list_dictionaries = []
    sorted_char_dictionary = {}
    for key in char_dict:
        if key.isalpha():
            sorted_char_dictionary = {}
            sorted_char_dictionary["character"] = key
            sorted_char_dictionary["count"] = char_dict[key]
            list_dictionaries.append(sorted_char_dictionary)
        else:
            continue
    list_dictionaries.sort(reverse=True, key=sort_on)
    return list_dictionaries