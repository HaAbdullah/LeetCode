# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k):
    
        # DFS through root, in order, with a counter variable 
            # when root is none, return 0 
            # counter is added each time
            # when counter = k, change res to root.val
            # 
        # reutrn root. val
        self.res = 0
        self.count = 0 
        def dfs(root):
            if not root: return None

            # go left as possible
            dfs(root.left)
            # visit it 
            self.count += 1
            if self.count == k:
                self.res = root.val
                return
            
            dfs(root.right)


        dfs(root)
        return self.res

# Helper function to build tree from array (LeetCode style)
def build_tree_from_array(arr):
    if not arr or arr[0] is None:
        return None
    
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    
    while queue and i < len(arr):
        node = queue.pop(0)
        
        # Left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test cases
def test_solution():
    solution = Solution()
    
    # Test case 1: root = [3,1,4,null,2], k = 1
    # Expected output: 1
    root1 = build_tree_from_array([3, 1, 4, None, 2])
    result1 = solution.kthSmallest(root1, 1)
    print(f"Test case 1 - root=[3,1,4,null,2], k=1: {result1} (expected: 1)")
    
    # Test case 2: root = [5,3,6,2,4,null,null,1], k = 3
    # Expected output: 3
    root2 = build_tree_from_array([5, 3, 6, 2, 4, None, None, 1])
    result2 = solution.kthSmallest(root2, 3)
    print(f"Test case 2 - root=[5,3,6,2,4,null,null,1], k=3: {result2} (expected: 3)")
    
    # Additional test cases
    # Test case 3: Single node, k=1
    root3 = build_tree_from_array([1])
    result3 = solution.kthSmallest(root3, 1)
    print(f"Test case 3 - root=[1], k=1: {result3} (expected: 1)")
    
    # Test case 4: root = [2,1,3], k=2
    root4 = build_tree_from_array([2, 1, 3])
    result4 = solution.kthSmallest(root4, 2)
    print(f"Test case 4 - root=[2,1,3], k=2: {result4} (expected: 2)")
    
    # Test case 5: root = [4,2,6,1,3,5,7], k=5
    root5 = build_tree_from_array([4, 2, 6, 1, 3, 5, 7])
    result5 = solution.kthSmallest(root5, 5)
    print(f"Test case 5 - root=[4,2,6,1,3,5,7], k=5: {result5} (expected: 5)")

if __name__ == "__main__":
    test_solution()