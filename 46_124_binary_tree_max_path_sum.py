# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        # Your solution here
        self.max_path_sum = float('-inf')
        
        def helper(node):
            if node is None: return 0
            left_max = max(0, helper(node.left))
            right_max = max(0, helper(node.right))
            path_sum = node.val +  left_max + right_max
            self.max_path_sum = max(path_sum, self.max_path_sum)
            
            return max(node.val + right_max, node.val + left_max)
            

        helper(root)
        return self.max_path_sum
        

# Test cases
def build_tree_1():
    """
    Tree:   1
           / \
          2   3
    Expected: 6 (path: 2 -> 1 -> 3)
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    return root

def build_tree_2():
    """
    Tree:     -10
             /   \
            9     20
                 /  \
                15   7
    Expected: 42 (path: 15 -> 20 -> 7)
    """
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

# Test your solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    tree1 = build_tree_1()
    result1 = solution.maxPathSum(tree1)
    print(f"Test 1 - Expected: 6, Got: {result1}")
    
    # Test case 2
    tree2 = build_tree_2()
    result2 = solution.maxPathSum(tree2)
    print(f"Test 2 - Expected: 42, Got: {result2}")