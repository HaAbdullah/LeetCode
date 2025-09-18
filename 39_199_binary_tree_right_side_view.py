from typing import Optional, List 
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root])
        res = []
        while q:
            lenQ = len(q)
            found_first = False
            for i in range(lenQ):
                node = q.popleft()
                if found_first is False: 
                    res.append(node.val)
                    found_first = True
                if node.right:
                    q.append(node.right)
                if node.left:
                        q.append(node.left)
        return res 