class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_list = defaultdict(list)

        for u, v, w in edges:
            adj_list[u].append((v,w))
        
        dist = [math.inf] * n
        pq = [(0, src)]
        dist[src] = 0

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in adj_list[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
            
        for i in range(n):
            if dist[i] == math.inf:
                dist[i] = -1
        
        return dict(zip(range(n), dist))
