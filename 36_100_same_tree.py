from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
        def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None: 
                return True 
            if p is None:
                return False 
            if q is None:
                return False
            if q.val != p.val: return False
            return True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Test Case 1: p = [1,2,3], q = [1,2,3] -> True
p1 = TreeNode(1)
p1.left = TreeNode(2)
p1.right = TreeNode(3)

q1 = TreeNode(1)
q1.left = TreeNode(2)
q1.right = TreeNode(3)

# Test Case 2: p = [1,2], q = [1,null,2] -> False
p2 = TreeNode(1)
p2.left = TreeNode(2)

q2 = TreeNode(1)
q2.right = TreeNode(2)

# Test Case 3: p = [1,2,1], q = [1,1,2] -> False
p3 = TreeNode(1)
p3.left = TreeNode(2)
p3.right = TreeNode(1)

q3 = TreeNode(1)
q3.left = TreeNode(1)
q3.right = TreeNode(2)

# Run tests
solution = Solution()
print(f"Test 1: {solution.isSameTree(p1, q1)}")  # Expected: True
print(f"Test 2: {solution.isSameTree(p2, q2)}")  # Expected: False
print(f"Test 3: {solution.isSameTree(p3, q3)}")  # Expected: False