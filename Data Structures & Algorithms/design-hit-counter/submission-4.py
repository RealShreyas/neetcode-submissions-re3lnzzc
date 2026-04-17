class HitCounter:

    def __init__(self):
        self.q = []
        

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        target = timestamp - 300

        l, r = 0, len(self.q)

        while l < r:
            m = (l+r) // 2
            if self.q[m] <= target:
                l = m+1
            else:
                r = m
        
        return len(self.q)-l
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
