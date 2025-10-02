def findRedundantConnection(edges):
    # for each edge, add the edge and see if it adds a cycle

    adjList = {i: [] for i in range(len(edges) + 1)}

    def dfs(node, parent):
        # undirected graph so remove the parent 
        visited.add(node)
        for neighbor in adjList[node]:
            if neighbor != parent:
                if neighbor in visited:
                    return True
                # now run dfs on all the real neighbors
                if dfs(neighbor, node):
                    return True
        return False
    for x, y in edges:
        adjList[x].append(y)
        adjList[y].append(x)
        visited = set ()
        # check if there is a cycle
        if dfs(x, -1):
            return [x, y]


print(findRedundantConnection(edges = [[1,2],[1,3],[2,3]]))
print(findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]))