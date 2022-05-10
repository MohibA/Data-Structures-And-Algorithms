class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set()
        
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor,node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n

        