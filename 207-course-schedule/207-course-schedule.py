class Solution:
    def explore(self,courseMap,course,visited):
        if course in visited:
            return False
        if courseMap[course] == []:
            return True
        
        visited.add(course)
        
        for prereq in courseMap[course]:
            if not self.explore(courseMap,prereq,visited):
                return False
        visited.remove(course)
        courseMap[course] = []
        
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
    
    
            
            