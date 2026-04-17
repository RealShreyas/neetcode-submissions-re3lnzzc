class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.snake = deque([(0,0)])
        self.occupied = {(0,0)}
        self.food_queue = deque([(f[0], f[1]) for f in food])
        self.score = 0

    def move(self, direction: str) -> int:
        directions = {'U': (-1,0), 'D': (1,0), 'L' : (0, -1), 'R': (0,1)}
        dr, dc = directions[direction]
        head_r, head_c = self.snake[0]
        new_head = (head_r + dr, head_c + dc)

        if not (0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width):
            return -1
        
        if self.food_queue and new_head == self.food_queue[0]:
            self.food_queue.popleft()
            self.score += 1
            self.snake.appendleft(new_head)
            self.occupied.add(new_head)
        else:
            if new_head in self.occupied:
                return -1
            
            self.snake.appendleft(new_head)
            self.occupied.add(new_head)
            tail = self.snake.pop()
            self.occupied.remove(tail)
        
        return self.score

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
