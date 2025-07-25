from typing import Optional, List 
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
            # create a queue with just root node 
        
            # while queue is not empty
                # get the length of the current queue
                # set found_first to false 
                # loop that many times and for each loop:   
                    # if found_first is False: add an element to res and then set found_first to True
                    # add the right node and then the left node of the current node 

            # return res 
            if not root: return None
            q = deque(root)
            res = []
            while q:
                lenQ = len(q)
                found_first = False
                for i in lenQ:
                    print("hi!")
                    node = q.popleft()
                    if not found_first: 
                        res.append(node)
                        found_first = True
                    if node.left:
                         q.append(node.left)
                    if node.right:
                         q.append(node.right)

            return res 