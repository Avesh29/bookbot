def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"Number of words in the book: {count_words(text)}")


def get_book_text(path):
    """Reads the content of the book from the given file path."""
    with open(path, 'r') as f:
        return f.read()


def count_words(text):
    """Counts the number of words in the given text."""
    words = text.split()  # Split the text by whitespace to get individual words
    return len(words)  # Return the length of the words list


main()


