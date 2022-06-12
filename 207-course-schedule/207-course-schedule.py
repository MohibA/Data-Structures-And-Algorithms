class Solution:
    def explore(self,courseMap,node,visited):
        if node in visited:
            return False
        if courseMap[node] == []:
            return True
        
        visited.add(node)
        
        for prereq in courseMap[node]:
            if not self.explore(courseMap,prereq,visited):
                return False
        visited.remove(node)
        courseMap[node] = []
        
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        visited = set()
        
        for i,j in prerequisites:
            courseMap[i].append(j)
        
        for course in range(numCourses):
            if not self.explore(courseMap,course,visited):
                return False
            
        return True
    
    
            
            