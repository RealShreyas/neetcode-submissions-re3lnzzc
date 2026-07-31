from typing import List

def count_unique_words(words: List[str]) -> int:
    hello = set()
    for i in words :
        hello.add(i)
    if len(hello) != 0 :
        return len(hello) 
    else :
        return 0
# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
