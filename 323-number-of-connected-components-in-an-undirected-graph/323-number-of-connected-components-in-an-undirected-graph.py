class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #Convert edges in to adjacency list
        # initialize counter variable at 0
        #Traverse over a node if not visited
        #incrase count
        
        if n <= 1:
            return 1
        
        count = 0
        
        graph = defaultdict(list)
        
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        stack, not_seen = [], set({i for i in range(n)})
        print(not_seen)
        counter = 0
        
        while not_seen:
            node = not_seen.pop()
            stack.append(node)
            counter += 1 
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor in not_seen:
                        not_seen.remove(neighbor)
                        stack.append(neighbor)
        
        return counter
        
        
        