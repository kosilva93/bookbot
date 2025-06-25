def get_num_words(file):
    words = file.split()
    num_words = len(words)
    return f"{num_words}"


def get_num_characters(file):
    file = file.lower()
    character_dict = {}

    for character in file:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    
    return character_dict


def sort_on(items):
    return items["num"]


def sort_dict(character_dict):
    char_list = []
    my_dict = {}

    for key, value in character_dict.items():
        char_list.append({"char": key, "num": value})

    char_list.sort(reverse=True, key=sort_on)

    for item in char_list:
        my_dict[item["char"]] = item["num"]
        
    # print(my_dict)
    return my_dict