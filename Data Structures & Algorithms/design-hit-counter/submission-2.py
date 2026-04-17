class HitCounter:

    def __init__(self):
        self.hits = []
        

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        target = timestamp-300

        l,r = 0, len(self.hits)

        while l < r:
            m = (l+r) // 2
            if self.hits[m] <= target:
                l = m+1
            else:
                r = m
        
        return len(self.hits)-l
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
