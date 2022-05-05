class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n <= 1:
            return True
        
        graph = defaultdict(list)
    
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set()
        stack = [source]
        
        while stack:
            currNode = stack.pop()
            for neighbor in graph[currNode]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    if neighbor == destination:
                        return True
        return False
        
        
        
        