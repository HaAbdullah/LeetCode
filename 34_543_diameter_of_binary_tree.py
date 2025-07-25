# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root):
        # diameter of a binary tree: the biggest left + right heights 
        self.result = 0
        def height(root):
            if root == None: return 0 
            left, right = height(root.left), height(root.right)
            self.result = max(left + right, self.result)
            return 1 + max(left, right)
        
        height(root)
        return self.result

# Test cases
def list_to_tree(lst):
    if not lst:
        return None
    
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    
    while queue and i < len(lst):
        node = queue.pop(0)
        
        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [1,2,3,4,5] -> 3
    root1 = list_to_tree([1,2,3,4,5])
    diameter1 = solution.diameterOfBinaryTree(root1)
    print("Test 1:", diameter1)
    
    # Test case 2: [1,2] -> 1
    root2 = list_to_tree([1,2])
    diameter2 = solution.diameterOfBinaryTree(root2)
    print("Test 2:", diameter2)