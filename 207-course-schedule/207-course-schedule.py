class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        visited = set()
        
        for i,j in prerequisites:
            courseMap[i].append(j)
        
        #visited Set
        def dfs(course):
            if course in visited:
                return False
            if courseMap[course] == []:
                return True
            
            visited.add(course)
            for prereq in courseMap[course]:
                if not dfs(prereq): return False
            
            visited.remove(course)
            courseMap[course] = []
            
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        
        return True
            