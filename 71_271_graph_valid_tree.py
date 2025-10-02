from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Quick check: a tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        # Build adjacency list
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:  # skip the edge back to parent
                    continue
                if neighbor in visited:  # cycle detected
                    return False
                if not dfs(neighbor, node):  # explore neighbor
                    return False
            return True

        # Start DFS from node 0 and check connectivity
        return dfs(0, -1) and len(visited) == n
