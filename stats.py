# returns the number of words in the string
def get_num_words(text): 
    words = text.split()
    num_words = len(words)
    return num_words

''' returns the number of times each character, 
    (including symbols and spaces), appears in the string
    '''
def get_num_characters(text): 
    chars_dict = {}
    lc_text = text.lower()
    chars_set = set(lc_text)
    for char in chars_set:
        chars_dict[char] = lc_text.count(char)

    return (chars_dict)

# used as key for sort
def sort_on(dict):
    
    return dict["num"]

# sorts dictionary alphabetical
def sort_dict(chars_dict):
    sorted_list = []
    
    for key, value in chars_dict.items():
        if key.isalpha():
            add_entry = {"char": key, "num": value}
            sorted_list.append(add_entry)
    
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
