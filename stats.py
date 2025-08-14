def sort_on(items):
    return items['num']

def print_report(file_path):
    with open(file_path) as file:
        return build_report(file.read(), file_path)

def build_report(text, file_path):
    words = text.split()
    dictionary = build_character_dictionary(words)
    sorted_list = convert_to_list(dictionary)
    word_count = len(words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for row in sorted_list:
        print(f"{row['char']}: {row['num']}")
    print("============= END ===============")

def build_character_dictionary(words):
    alpha = {}

    for word in words:
        string = list(word.lower())
        for char in string:
            if char in alpha:
                count = alpha[char]
                count += 1
                alpha[char] = count
            else:
                alpha[char] = 1
    return alpha

def convert_to_list(dictionary):
    pre_sorted_list = []
    for char in dictionary:
        if(char.isalpha()):
            touple = {}
            touple['char'] = char
            touple['num'] = dictionary[char]
            pre_sorted_list.append(touple)
    
    return sorted(pre_sorted_list, reverse=True, key=sort_on)