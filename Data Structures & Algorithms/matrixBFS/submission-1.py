from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1
            
        m, n = len(grid), len(grid[0])
        # Use a set to keep track of visited cells to prevent cycles and redundant work
        visited = set([(0, 0)])
        queue = deque([(0, 0, 0)]) # Store (x, y, distance)

        while queue:
            x, y, dist = queue.popleft()
            
            # Reached target
            if x == m - 1 and y == n - 1:
                return dist
            
            # Explore neighbors
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
        
        return -1
                            