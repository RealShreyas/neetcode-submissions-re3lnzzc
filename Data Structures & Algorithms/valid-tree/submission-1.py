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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        dsu = UnionFind()

        for u, v in edges:
            if not dsu.union(u,v):
                return False
        
        return True
        