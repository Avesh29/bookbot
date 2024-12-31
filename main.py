def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    # Get word and character counts
    word_count = count_words(text)
    character_counts = count_characters(text)
    
    # Print the report
    print_report(book_path, word_count, character_counts)


def get_book_text(path):
    """Reads the content of the book from the given file path."""
    with open(path, 'r') as f:
        return f.read()


def count_words(text):
    """Counts the number of words in the given text."""
    words = text.split()  # Split the text by whitespace to get individual words
    return len(words)  # Return the length of the words list


def count_characters(text):
    """Counts the frequency of each character in the given text."""
    text = text.lower()  # Convert all characters to lowercase
    character_count = {}  # Dictionary to store character counts
    
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
                
    return character_count  # Return the dictionary of character counts


def print_report(path, word_count, character_counts):
    """Prints a formatted report with word and character data."""
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    
    # Convert the character counts dictionary into a sorted list of tuples
    sorted_characters = sorted(character_counts.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")


main()






