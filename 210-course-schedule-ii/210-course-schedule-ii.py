class Solution:
    def explore(self,courseMap,course,visited,cycle,output):
        if course in cycle:
            return False
        if course in visited:
            return True
        
        cycle.add(course)
        
        for pre in courseMap[course]:
            if not self.explore(courseMap,pre,visited,cycle,output):
                return False
            
        cycle.remove(course)
        visited.add(course)
        output.append(course)
        
        return True
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = defaultdict(list)
        visited = set()
        cycle = set()
        output = []
        
        
        for course,preReq in prerequisites:
            courseMap[course].append(preReq)
        
        #Loop over numCourses and run explore function
        for course in range(numCourses):
            if not self.explore(courseMap,course,visited,cycle,output):
                return []
        return output
        
        
        