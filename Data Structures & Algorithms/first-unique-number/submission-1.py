class FirstUnique:

    def __init__(self, nums: List[int]):
        self.mp = {}
        self.q = deque()

        for num in nums:
            self.add(num)     

    def showFirstUnique(self) -> int:
        while self.q and not self.mp[self.q[0]]:
            self.q.popleft()
        
        if self.q:
            return self.q[0]
        
        return -1

    def add(self, value: int) -> None:
        if value not in self.mp:
            self.mp[value] = True
            self.q.append(value)
        else:
            self.mp[value] = False


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
