class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.component_size = [1] * n
        self.num_of_components = n
    
    def find(self, p):
        if p != self.parents[p]:
            self.parents[p] = self.find(self.parents[p])
        
        return self.parents[p]
    
    def get_connected_components(self):
        return self.num_of_components
    
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q:
            return
        
        if self.component_size[root_p] < self.component_size[root_q]:
            self.component_size[root_q] += self.component_size[root_p]
            self.parents[root_p] = root_q
        else:
            self.component_size[root_p] += self.component_size[root_q]
            self.parents[root_q] = root_p

        self.num_of_components -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)

        for u, v in edges:
            dsu.union(u, v)
        
        return dsu.get_connected_components()
        