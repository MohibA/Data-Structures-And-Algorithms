class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        #build graph
        graph = defaultdict(list)
        
        for i,j in roads:
            graph[i].append(j)
            graph[j].append(i)
        
        result = 0
        
        #traverse over cities to calculate max network
        #to get max network add lenghts of city 1 and 2 and subtract 1 if city 1 in city2 since their connecting road is only counted once
        for city1 in range(n):
            for city2 in range(city1+1,n):
                current = (len(graph[city1]) + len(graph[city2]) - (1 if city1 in graph[city2] else 0))
                result = max(result,current)
        return result
        