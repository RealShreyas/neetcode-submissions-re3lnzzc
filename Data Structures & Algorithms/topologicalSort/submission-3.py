class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_deg = [0] * n

        for u, v in edges:
            adj_list[u].append(v)
            in_deg[v] += 1
        
        top_sort = []
        q = deque()

        for i in range(n):
            if in_deg[i] == 0:
                q.append(i)
        
        while q:
            u = q.popleft()
            top_sort.append(u)

            for v in adj_list[u]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    q.append(v)
        
        return [] if len(top_sort) != n else top_sort
         