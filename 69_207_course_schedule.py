def canFinish(numCourses, prerequisites):
    # create adjacency list
    adjList = {i: [] for i in range(numCourses)}

    for course, prerequisite in prerequisites:
            adjList[prerequisite].append(course)
            
    # dfs each node and mark every path node as path so you know if you visit it again (after exploring its neighbors) that there is a cycle
    visited = set()
    path = set()
    def dfs(course):
        # cycle detected
        if course in path:
            return False 
        if course in visited:
            return True
        path.add(course)
        for neigbor in adjList[course]:
            # only return False if one of them is False, if its true dont break and return, keep going 
            if not dfs(neigbor):
                return False
        path.remove(course)
        visited.add(course)
        return True
    
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True
print(canFinish(numCourses = 2, prerequisites = [[1,0]]))