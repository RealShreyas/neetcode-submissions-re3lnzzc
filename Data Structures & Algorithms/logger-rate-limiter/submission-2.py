class Logger:

    def __init__(self):
        self.q = deque([])
        self.msg = set()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.q and timestamp - self.q[0][1] >= 10:
            m, t = self.q.popleft()
            if m in self.msg:
                self.msg.remove(m)

        if message in self.msg:
            return False

        self.q.append((message, timestamp))
        self.msg.add(message)

        return True

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
