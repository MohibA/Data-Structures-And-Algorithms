class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        
        graph = defaultdict(list)
        
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def explore(node):
            visited.add(node)
        
            for neighbor in graph[node]:
                if neighbor not in visited:
                    explore(neighbor)
        
        visited = set()
        
        for i in range(n):
            if i not in visited:
                explore(i)
                count += 1
        return count
    

        
    
        
        