class Logger:

    def __init__(self):
        self.log = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        should_print = False
        if message in self.log:
            if timestamp - self.log[message] >= 10:
                should_print = True
                self.log[message] = timestamp
        else:
            should_print = True
            self.log[message] = timestamp
        
        return should_print

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
