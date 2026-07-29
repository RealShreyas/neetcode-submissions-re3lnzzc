def remove_fourth_character(word: str) -> str:
    before_fourth = (word[:3])
    fourth_character = (word[3:4])
    rest = (word[4:])
    return before_fourth + rest
# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
