class StringIterator:

    def __init__(self, compressedString: str):
        self.char_count_pairs = []
        self.current_index = 0

        n = len(compressedString)
        i = 0

        while i < n:
            char = compressedString[i]
            i += 1

            count = 0
            while i < n and compressedString[i].isdigit():
                count *= 10
                count += int(compressedString[i])
                i += 1
            
            self.char_count_pairs.append([char, count])


    def next(self) -> str:
        if not self.hasNext():
            return ' '
        
        result_char = self.char_count_pairs[self.current_index][0]
        self.char_count_pairs[self.current_index][1] -= 1

        if self.char_count_pairs[self.current_index][1] == 0:
            self.current_index += 1
        
        return result_char
         

    def hasNext(self) -> bool:
        return (self.current_index < len(self.char_count_pairs) and self.char_count_pairs[self.current_index][1] > 0)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
