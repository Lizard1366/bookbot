def get_num_words(file_path):
    with open(file_path) as file:
        return count_book_words(file.read())

def count_book_words(text):
    words = text.split()
    print(f"{len(words)} words found in the document")  