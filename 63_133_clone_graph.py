
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def __init__(self):
        self.visitedNodes = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # create a headnode that is a copy of the given node with same value, but no neighbors 
        
        if not node: return None 


        # Option 1: we have already created this specific node
        if node in self.visitedNodes:
            return self.visitedNodes[node]

        # Option 2: we must create this node and its neighbors   
        head = Node(node.val)
        self.visitedNodes[node] = head
        for neigbor in node.neighbors:
            head.neighbors.append(self.cloneGraph(neigbor))

        return head