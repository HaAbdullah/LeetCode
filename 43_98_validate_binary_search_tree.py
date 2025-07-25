# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):

        def DFS(root, left_leader=None, right_leader=None):
            if not root: return True


            if right_leader is not None and root.val >= right_leader: return False
            if left_leader is not None and root.val <= left_leader: return False
            
            return DFS(root.left, left_leader, root.val) and DFS(root.right, root.val, right_leader)
        
        return DFS(root, None, None)
        # sub function that tracks left leader and right leader, and returns any time that current node <= left parent (leader) or >= right parent (leader)
        # other wise return the two branches AND each other 
        # if you reach the end (None node), then return True 


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
    
    # Test case 1: [2,1,3] - Expected: True
    root1 = build_tree_from_array([0, None, -1])
    result1 = solution.isValidBST(root1)
    print(f"Test case 1 [2,1,3]: {result1} (expected: True)")
    
    # # Test case 2: [5,1,4,null,null,3,6] - Expected: False
    # root2 = build_tree_from_array([5, 1, 4, None, None, 3, 6])
    # result2 = solution.isValidBST(root2)
    # print(f"Test case 2 [5,1,4,null,null,3,6]: {result2} (expected: False)")
    
    # # Additional test cases
    # # Test case 3: [1] - Expected: True
    # root3 = build_tree_from_array([1])
    # result3 = solution.isValidBST(root3)
    # print(f"Test case 3 [1]: {result3} (expected: True)")
    
    # # Test case 4: [1,1] - Expected: False (duplicate values)
    # root4 = build_tree_from_array([1, 1])
    # result4 = solution.isValidBST(root4)
    # print(f"Test case 4 [1,1]: {result4} (expected: False)")
    
    # # Test case 5: [] - Expected: True
    # root5 = build_tree_from_array([])
    # result5 = solution.isValidBST(root5)
    # print(f"Test case 5 []: {result5} (expected: True)")

if __name__ == "__main__":
    test_solution()