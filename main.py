def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        text = f.read()
        num_words = get_word_count(text)
        character_count = get_character_count(text)
        character_list = convert_dict_to_list(character_count)
        character_list.sort(reverse=True, key=sort_on)
        print(f"--- Begin report of {book_path} ---")
        print(f"{num_words} words found in the document\n")
        for character in character_list:
            print(f"The '{character["character"]}' character was found {character["count"]} times")
        print("--- End report ---")

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_count = {}
    for character in text:
        lowercase_character = character.lower()
        if lowercase_character not in character_count:
            character_count[lowercase_character] = 1
        else:
            character_count[lowercase_character] += 1
    return character_count

def convert_dict_to_list(dict):
    character_count_list = []
    for character in dict:
        if character.isalpha():
            character_count_list.append({"character": character, "count": dict[character]})
    return character_count_list


def sort_on(dict):
    return dict["count"]

main()
