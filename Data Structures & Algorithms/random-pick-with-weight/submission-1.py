import bisect 

class Solution:

    def __init__(self, w: List[int]):
        self.pref = [0]
        for weight in w:
            self.pref.append(self.pref[-1] + weight)

    def pickIndex(self) -> int:
        val = random.randint(1, self.pref[-1])
        idx = bisect.bisect_left(self.pref, val)
        return idx-1
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()