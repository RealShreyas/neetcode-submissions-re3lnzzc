class UnionFind:
    def __init__(self):
        self.parents = {}
        self.component_size = {}
        self.num_of_components = 0
    
    def find(self, p):
        if p not in self.parents:
            self.parents[p] = p
            self.component_size[p] = 1
            self.num_of_components += 1
        
        if p == self.parents[p]:
            return p
        
        self.parents[p] = self.find(self.parents[p])

        return self.parents[p]
    
    def union(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)

        if root1 == root2:
            return
        
        if self.component_size[root1] < self.component_size[root2]:
            self.parents[root1] = root2
            self.component_size[root2] += self.component_size[root1]
        else:
            self.parents[root2] = root1
            self.component_size[root1] += self.component_size[root2]
        
        self.num_of_components -= 1
    
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
        


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind()
        edges.sort(key = lambda x: x[2])
        mst_cost = 0
        edge_count = 0

        for u, v, w in edges:
            if not dsu.is_connected(u, v):
                dsu.union(u,v)
                mst_cost += w
                edge_count += 1

                if edge_count == n-1:
                    return mst_cost
        
        return -1

