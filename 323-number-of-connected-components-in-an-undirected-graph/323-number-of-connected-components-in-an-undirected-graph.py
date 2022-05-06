class Solution:
    def explore(self,graph,node,visited):
        if node in visited:
            return False
        
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                self.explore(graph,neighbor,visited)
        return True
                
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        
        graph = defaultdict(list)
        
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set()
        
        for i in range(n):
            if i not in visited:
                self.explore(graph,i,visited)
                count += 1
        return count
    
        
    
        
        