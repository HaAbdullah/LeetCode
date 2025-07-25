# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        res = 0 
        if root is None:
            return 0
        
        # max of root is going to be max of two subtrees
        res = max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
        return res
    
    def maxDepth(self, root):
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.left))
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
    
    # Test case 1: [3,9,20,null,null,15,7] -> 3
    root1 = list_to_tree([3,9,20,None,None,15,7])
    depth1 = solution.maxDepth(root1)
    print("Test 1:", depth1)
    
    # Test case 2: [1,null,2] -> 2
    root2 = list_to_tree([1,None,2])
    depth2 = solution.maxDepth(root2)
    print("Test 2:", depth2)