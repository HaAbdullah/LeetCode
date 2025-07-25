# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math
class Solution:
    def isBalanced(self, root):
        # call getHeights() on left and right nodes and check if they equal within 1 of each other
        # 
        self.res = True
        def getHeight(curr):
            if curr is None or self.res == False: 
                return 0 
            
            left_height = getHeight(curr.left)
            right_height = getHeight(curr.right)
            
            #print(f"left: {left_height} right: {right_height}")
            if abs(left_height - right_height) > 1:
                #print("wowzers")
                self.res = False
                return 0
            
            return 1 + max(left_height, right_height)
        getHeight(root)
        return self.res

# Helper function to build tree from array representation
def build_tree(arr):
    if not arr or arr[0] is None:
        return None
    
    nodes = [TreeNode(val) if val is not None else None for val in arr]
    root = nodes[0]
    
    for i in range(len(arr)):
        if nodes[i] is not None:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            
            if left_idx < len(nodes):
                nodes[i].left = nodes[left_idx]
            if right_idx < len(nodes):
                nodes[i].right = nodes[right_idx]
    
    return root

# Test cases
def test_solution():
    solution = Solution()
    
    # Test case 1: Balanced tree
    # Tree: [3,9,20,null,null,15,7]
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    result1 = solution.isBalanced(root1)
    print(f"Test 1 - Expected: True, Got: {result1}")
    
    # Test case 2: Unbalanced tree
    # Tree: [1,2,2,3,3,null,null,4,4]
    root2 = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    result2 = solution.isBalanced(root2)
    print(f"Test 2 - Expected: False, Got: {result2}")
    
    # Test case 3: Empty tree
    root3 = build_tree([])
    result3 = solution.isBalanced(root3)
    print(f"Test 3 - Expected: True, Got: {result3}")
    
    # Test case 4: Single node
    root4 = build_tree([1])
    result4 = solution.isBalanced(root4)
    print(f"Test 4 - Expected: True, Got: {result4}")

if __name__ == "__main__":
    test_solution()