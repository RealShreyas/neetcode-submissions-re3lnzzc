class UnionFind:
    def __init__(self):
        self.parents = {}
        self.component_size = {}
        self.no_of_components = 0
    
    def find(self, p):
        if p not in self.parents:
            self.parents[p] = p
            self.component_size[p] = 1
            self.no_of_components += 1
        
        root = self.parents[p]

        if root != p:
            self.parents[p] = self.find(root)
        
        return root
    
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q:
            return
        
        if self.component_size[p] > self.component_size[q]:
            self.parents[q] = root_p
            self.component_size[p] += self.component_size[q]
        else:
            self.parents[p] = root_q
            self.component_size[q] += self.component_size[p]
        
        self.no_of_components -= 1
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        dsu = UnionFind()
        logs.sort(key = lambda x : x[0])

        for i in range(n):
            dsu.find(i)

        for t, a, b in logs:
            dsu.union(a,b)
            if dsu.no_of_components == 1:
                return t

        return -1

        