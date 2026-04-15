class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(0,0)])

        path = 0

        while len(queue) > 0:
            sz = len(queue)
            path += 1
            for _ in range(sz):
                x, y = queue.popleft()
                if x == m-1 and y == n-1:
                    return path-1
                for dx, dy in [(0, 1), (1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 1:
                        queue.append((nx,ny))
        
        return -1
                            