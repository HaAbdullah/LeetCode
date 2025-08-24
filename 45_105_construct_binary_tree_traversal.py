# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # base case: if preorder is none or inorder is none: return none
        if len(preorder) == 0 or len(inorder) == 0 : return None
        # first element of preorder is root 
        root = TreeNode(preorder[0])
        # find the root in the inorder array
            # two insights can be found from the index:
                # 1. All elements to the left of index are at the left of the root, and all elements to the right of the index are at the right of the root
                # 2. The index is the number of elements that are in the left side of the tree (how many elements we can skiip for the next recursion.right)
        mid = inorder.index(preorder[0])
        # root.left = buildTree(preorder[1:mid+1], inorder[:mid])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # root.right = buildTree(preorder[mid+1:], inorder[mid + 1:])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        # return root
        
        return root
# Helper function to convert tree to array for easy comparison
def tree_to_array(root):
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

# Helper function to print tree structure (for visualization)
def print_tree_structure(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            if root.left:
                print_tree_structure(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree_structure(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

# Test cases
def test_solution():
    solution = Solution()
    
    # Test case 1: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    # Expected tree structure:
    #       3
    #      / \
    #     9   20
    #        /  \
    #       15   7
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    
    print("Test Case 1:")
    print(f"Preorder: {preorder1}")
    print(f"Inorder:  {inorder1}")
    
    result1 = solution.buildTree(preorder1, inorder1)
    result_array1 = tree_to_array(result1)
    print(f"Result array: {result_array1}")
    print(f"Expected:     [3, 9, 20, None, None, 15, 7]")
    print("Tree structure:")
    print_tree_structure(result1)
    print("-" * 50)
    
    # Test case 2: preorder = [-1], inorder = [-1]
    # Expected: single node tree with value -1
    preorder2 = [-1]
    inorder2 = [-1]
    
    print("Test Case 2:")
    print(f"Preorder: {preorder2}")
    print(f"Inorder:  {inorder2}")
    
    result2 = solution.buildTree(preorder2, inorder2)
    result_array2 = tree_to_array(result2)
    print(f"Result array: {result_array2}")
    print(f"Expected:     [-1]")
    print("Tree structure:")
    print_tree_structure(result2)
    print("-" * 50)
    
    # Test case 3: More complex tree
    # preorder = [1,2,4,5,3,6,7], inorder = [4,2,5,1,6,3,7]
    preorder3 = [1, 2, 4, 5, 3, 6, 7]
    inorder3 = [4, 2, 5, 1, 6, 3, 7]
    
    print("Test Case 3:")
    print(f"Preorder: {preorder3}")
    print(f"Inorder:  {inorder3}")
    
    result3 = solution.buildTree(preorder3, inorder3)
    result_array3 = tree_to_array(result3)
    print(f"Result array: {result_array3}")
    print("Tree structure:")
    print_tree_structure(result3)
    print("-" * 50)

if __name__ == "__main__":
    test_solution()