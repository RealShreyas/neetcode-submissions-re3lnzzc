class MovingAverage:

    def __init__(self, size: int):
        self.window = deque([])
        self.size = size
        self.ans = 0
        

    def next(self, val: int) -> float:
        self.window.append(val)
        self.ans += val
        if len(self.window) > self.size:
            self.ans -= self.window.popleft()
        return self.ans / len(self.window)

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
