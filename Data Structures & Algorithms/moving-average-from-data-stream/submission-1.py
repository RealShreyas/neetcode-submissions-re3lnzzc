from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        # maxlen automatically pops the oldest element when a new one is added
        self.window = deque(maxlen=size)
        self.running_sum = 0
        

    def next(self, val: int) -> float:
        # If the window is full, the element about to be popped is at index 0
        if len(self.window) == self.window.maxlen:
            self.running_sum -= self.window[0]
            
        self.window.append(val)
        self.running_sum += val
        
        return self.running_sum / len(self.window)