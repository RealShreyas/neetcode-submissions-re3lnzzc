from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    char = {}
    for letter in word :
        if letter in char:
            char[letter] += 1
        else:
            char[letter] = 1
    return char




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
