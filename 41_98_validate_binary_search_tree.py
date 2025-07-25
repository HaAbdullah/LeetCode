# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        if not root: return True

   
        if root.val <= root.val or root.val >= root.val: return False 

        return self.isValidBST(root.left) and self.isValidBST(root.right)
        

# Test cases
def create_test_tree_1():
    # Tree: [2,1,3]
    #       2
    #      / \
    #     1   3
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    return root

def create_test_tree_2():
    # Tree: [5,1,4,null,null,3,6]
    #       5
    #      / \
    #     1   4
    #        / \
    #       3   6
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    return root

# Test your solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1 - should return True
    tree1 = create_test_tree_1()
    result1 = solution.isValidBST(tree1)
    print(f"Test case 1: {result1} (expected: True)")
    
    # Test case 2 - should return False
    tree2 = create_test_tree_2()
    result2 = solution.isValidBST(tree2)
    print(f"Test case 2: {result2} (expected: False)")
    
    # Edge case - single node
    single_node = TreeNode(1)
    result3 = solution.isValidBST(single_node)
    print(f"Single node test: {result3} (expected: True)")
    
    # Edge case - None/empty tree
    result4 = solution.isValidBST(None)
    print(f"Empty tree test: {result4} (expected: True)")