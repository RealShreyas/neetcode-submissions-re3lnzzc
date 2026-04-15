class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
        
        def dfs(cur, visited):
            if visited[cur] != None:
                return visited[cur] == 2
            
            if len(adj_list[cur]) == 0:
                return cur == destination
            
            visited[cur] = 1

            for next_node in adj_list[cur]:
                if not dfs(next_node, visited):
                    return False
            
            visited[cur] = 2
            return True
            
        
        return dfs(source, [None]*n)