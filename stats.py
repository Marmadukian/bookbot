
def sort_on(items):
    return items["num"]



def get_num_words(text):
    split_into_words = text.split()
    return len(split_into_words)

def get_character_count(text):
    total_count = {}
    for character in text:
        lower_char = character.lower()
        count = 0
        if total_count.get(lower_char):
            count = total_count.get(lower_char)
        count += 1
        total_count[lower_char] = count
    return total_count

def sort_char_count(char_count):
    split_dict = split_dictionary_to_array(char_count)
    split_dict.sort(reverse=True, key=sort_on)
    return split_dict

def split_dictionary_to_array(dict):
    splited = []
    for key in dict:
        split_dict = {}
        split_dict["char"] = key
        split_dict["num"] = dict[key]
        splited.append(split_dict)
    return splited
