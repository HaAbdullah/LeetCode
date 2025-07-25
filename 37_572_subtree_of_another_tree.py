from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # DFS through root
        # if you find a None node, return false
        # if node value == subnode value:
            # return check_same(node, sunode) or isSubtree(left) or isSubtree(right)
        # return isSubtree(left) or isSubtree(right)
        if not root: return False
        
        def check_same(p, q):
            if not p and not q: return True 
            if (not p or not q) or p.val != q.val : return False 
            return (check_same(p.left, q.left) and check_same(p.right, q.right))
        
        if root.val == subRoot.val and check_same(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)    

# Test Case 1: root = [3,4,5,1,2], subRoot = [4,1,2] -> True
root1 = TreeNode(3)
root1.left = TreeNode(4)
root1.right = TreeNode(5)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(2)

subRoot1 = TreeNode(4)
subRoot1.left = TreeNode(1)
subRoot1.right = TreeNode(2)

# Test Case 2: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] -> False
root2 = TreeNode(3)
root2.left = TreeNode(4)
root2.right = TreeNode(5)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(2)
root2.left.left.right = TreeNode(0)

subRoot2 = TreeNode(4)
subRoot2.left = TreeNode(1)
subRoot2.right = TreeNode(2)

# Run tests
solution = Solution()
print(f"Test 1: {solution.isSubtree(root1, subRoot1)}")  # Expected: True
print(f"Test 2: {solution.isSubtree(root2, subRoot2)}")  # Expected: False