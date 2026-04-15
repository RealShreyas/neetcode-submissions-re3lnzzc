class FirstUnique:

    def __init__(self, nums: List[int]):
        self._q = deque(nums)
        self._mp = {}

        for num in nums:
            self.add(num)
        

    def showFirstUnique(self) -> int:
        while self._q and not self._mp[self._q[0]]:
            self._q.popleft()
        
        if self._q:
            return self._q[0]
        
        return -1
        

    def add(self, value: int) -> None:
        if value not in self._mp:
            self._mp[value] = True
            self._q.append(value)
        else:
            self._mp[value] = False
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
