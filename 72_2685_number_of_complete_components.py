def countComponents(n, edges):
    adjList = {i : [] for i in range(n)}
    for x, y in edges:
        adjList[x].append(y)
        adjList[y].append(x)

    visited = set()

    def dfs(node):
        if node in visited:
            return 
        
        visited.add(node)

        for neighbor in adjList[node]:
            dfs(neighbor)
    count = 0 
    for i in range(n):
        if i not in visited: 
            dfs(i) 
            count += 1
    return count 


print(countComponents(n=3, edges=[[0,1], [0,2]]))