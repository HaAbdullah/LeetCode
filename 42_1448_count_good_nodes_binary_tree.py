# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(root, max):
            # if root is >= max: make max = root and += 1 res 
            # dfs(root.left, max), dfs(root.right, max)
            # if you reach None, return 

            if not root: return 
            if root.val >= max: 
                max = root.val
                self.res += 1
            dfs(root.left, max)
            dfs(root.right, max)

        dfs(root, 0)

        return self.res



# Helper function for testing
def build_tree(arr):
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    
    while queue and i < len(arr):
        node = queue.pop(0)
        
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test cases
def test():
    solution = Solution()
    
    # Test case 1
    root1 = build_tree([3,1,4,3,None,1,5])
    result1 = solution.goodNodes(root1)
    print(f"Test 1: Expected 4, Got {result1}")
    
    # Test case 2
    root2 = build_tree([3,3,None,4,2])
    result2 = solution.goodNodes(root2)
    print(f"Test 2: Expected 3, Got {result2}")

if __name__ == "__main__":
    test()