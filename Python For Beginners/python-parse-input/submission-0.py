from typing import List

def read_integers() -> List[int]:
    numbers = input()
    list_numbers = numbers.split(",")
    list_numbers = [int(i) for i in list_numbers]
    return(list_numbers)

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
