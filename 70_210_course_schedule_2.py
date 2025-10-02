def findOrder(numCourses, prerequisites):
        adjList = { x : [] for x in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
            
        res = []
        visited = set()
        path = set()
        def dfs(course):
            if course in path: return False 
            if course in visited: return True
            
            path.add(course)
            for prerequisite in adjList[course]:
                if not dfs(prerequisite): return False
                
            path.remove(course)
            visited.add(course)
            res.append(course)
            return True
        for i in range(numCourses):
            # if the dfs returns false, return false, otherwise move onto the next neighbor
            if not dfs(i): return []
        return res 
    
    
print(findOrder(numCourses = 3, prerequisites = [[1,0]]))