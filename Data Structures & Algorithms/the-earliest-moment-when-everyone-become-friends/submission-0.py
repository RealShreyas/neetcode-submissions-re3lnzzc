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
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        dsu = UnionFind()

        for i in range(n):
            dsu.find(i)
        
        for log in logs:
            dsu.union(log[1], log[2])
            if dsu.components == 1:
                return log[0]
        
        return -1

        