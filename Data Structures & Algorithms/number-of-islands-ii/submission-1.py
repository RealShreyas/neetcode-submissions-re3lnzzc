class UnionFind:
    def __init__(self):
        self.parents = {}
        self.component_size = {}
        self.components = 0
    
    def find(self, p):
        if p not in self.parents:
            self.parents[p] = p
            self.component_size[p] = 1
            self.components += 1
            return p
        
        if p == self.parents[p]:
            return p

        self.parents[p] = self.find(self.parents[p])
        return self.parents[p]
    
    def union(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)

        if root1 == root2:
            return False
        
        if self.component_size[root1] > self.component_size[root2]:
            self.parents[root2] = root1
            self.component_size[root1] += self.component_size[root2]
        else:
            self.parents[root1] = root2
            self.component_size[root2] += self.component_size[root1]
        self.components -= 1

        return True

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ans = []
        dsu = UnionFind()

        grid = [[0] * n for _ in range(m)]

        for i, j in positions:
            dsu.union((i,j), (i,j))
            grid[i][j] = 1

            if i-1 >= 0 and grid[i-1][j] == 1:
                dsu.union((i,j), (i-1,j))
            if j-1 >= 0 and grid[i][j-1] == 1:
                dsu.union((i,j), (i,j-1))
            if i+1 < m and grid[i+1][j] == 1:
                dsu.union((i,j), (i+1,j))
            if j+1 < n and grid[i][j+1] == 1:
                dsu.union((i,j), (i,j+1))
            
            ans.append(dsu.components)
        
        return ans

        