import bisect 

class Solution:

    def __init__(self, w: List[int]):
        self.pref = [0]
        for weight in w:
            self.pref.append(self.pref[-1] + weight)

    def pickIndex(self) -> int:
        val = random.randint(1, self.pref[-1])
        l, r = 1, len(self.pref)

        while l < r:
            m = (l+r) // 2
            if self.pref[m] >= val:
                r = m
            else:
                l = m+1
        
        return l-1
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()