class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.component_size = [1]*n
        self.no_of_components = n
    
    def find(self, p):
        if self.parents[p] != p:
            self.parents[p] = self.find(self.parents[p])
        
        return self.parents[p]
    
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q:
            return
        
        if self.component_size[root_p] > self.component_size[root_q]:
            self.parents[root_q] = root_p
            self.component_size[root_p] += self.component_size[root_q]
        else:
            self.parents[root_p] = root_q
            self.component_size[root_q] += self.component_size[root_p]
        
        self.no_of_components -= 1
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        if n == 1: return 0

        dsu = UnionFind(n)
        logs.sort(key = lambda x : x[0])

        for i in range(n):
            dsu.find(i)

        for t, a, b in logs:
            dsu.union(a,b)
            if dsu.no_of_components == 1:
                return t

        return -1

        