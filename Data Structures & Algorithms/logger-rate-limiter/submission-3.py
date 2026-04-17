class Logger:

    def __init__(self):
        self.window_size = 10
        self.messages = [set() for _ in range(self.window_size)]
        self.message_timestamp = [-1] * self.window_size
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        idx = timestamp % self.window_size

        if self.message_timestamp[idx] != timestamp:
            self.messages[idx].clear()
            self.message_timestamp[idx] = timestamp
        
        for i in range(self.window_size):
            if timestamp - self.message_timestamp[i] < self.window_size:
                if message in self.messages[i]:
                    return False

        self.messages[idx].add(message)
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
