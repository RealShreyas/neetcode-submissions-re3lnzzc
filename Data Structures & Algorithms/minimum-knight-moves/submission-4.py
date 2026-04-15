class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

        visited = set((0,0))
        queue = deque([(0,0)])
        x, y = abs(x), abs(y)

        moves = 0

        while len(queue) > 0:
            sz = len(queue)

            for _ in range(sz):
                i, j = queue.popleft()

                if i == x and y == j:
                    return moves
                
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if (ni, nj) not in visited:
                        visited.add((ni, nj))
                        queue.append((ni, nj))
            
            moves += 1
        
        return -1