# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # Step 1: Find a candidate
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                # If candidate knows i, 'candidate' is out, 'i' is the new lead
                candidate = i
        
        # Step 2: Verify the candidate
        for i in range(n):
            if i == candidate:
                continue
            # Celebrity must be known by everyone AND know no one
            if knows(candidate, i) or not knows(i, candidate):
                return -1
                
        return candidate
        