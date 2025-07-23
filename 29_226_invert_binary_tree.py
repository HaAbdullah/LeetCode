# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if root is None:
            return None
 
        # create temp left 

        temp_left = root.left
        # make left equal to the right
        root.left = root.right
        # make right equal to the temp left 
        root.right = temp_left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


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

def tree_to_list(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
    root1 = list_to_tree([4,2,7,1,3,6,9])
    inverted1 = solution.invertTree(root1)
    print("Test 1:", tree_to_list(inverted1))
    
    # Test case 2: [2,1,3] -> [2,3,1]
    root2 = list_to_tree([2,1,3])
    inverted2 = solution.invertTree(root2)
    print("Test 2:", tree_to_list(inverted2))
    
    # Test case 3: [] -> []
    root3 = list_to_tree([])
    inverted3 = solution.invertTree(root3)
    print("Test 3:", tree_to_list(inverted3))