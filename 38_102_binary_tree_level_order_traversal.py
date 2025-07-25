from typing import List, Optional 
from collections import deque 


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # dequeue with just root node 
        # while queue is not empty:
            # loop through the number of elements currently in the queue 
                # each node, add its children to the resulting set, and then pop it 
        # return res 
        q = deque()
        res = []
        if root: 
            q.append(root)
            

            q = deque([root])
        while q:
            current_level = []
            for i in range(len(q)):
                current_node = q.popleft()
                current_level.append(current_node.val)
                if current_node.left:
                    q.append(current_node.left)                
                if current_node.right:
                    q.append(current_node.right)
            if len(current_level): res.append(current_level)

        return res