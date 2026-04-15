class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_deg = [0] * n
 
        for u, v in edges:
            adj_list[u].append(v)
            in_deg[v] += 1
        
        ans = []

        queue = deque()

        for i in range(n):
            if in_deg[i] == 0:
                queue.append(i)
        
        while len(queue) > 0:
            u = queue.popleft()
            ans.append(u)
            for v in adj_list[u]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    queue.append(v)
        
        return ans if len(ans) == n else []
         