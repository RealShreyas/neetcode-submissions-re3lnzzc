class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        edge_count = 0
        mst_cost = 0

        for u, v, w in edges:
            adj_list[u].append([v,w])
            adj_list[v].append([u,w])

        pq = []
        visited = [False] * n

        heapq.heappush(pq, (0, 0))

        while pq:
            wt, u = heapq.heappop(pq)

            if visited[u]:
                continue
            
            visited[u] = True
            edge_count += 1
            mst_cost += wt

            for v, c in adj_list[u]:
                if not visited[v]:
                    heapq.heappush(pq, (c, v))
        
        return mst_cost if edge_count == n else -1
        