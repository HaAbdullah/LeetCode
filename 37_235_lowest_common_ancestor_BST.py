# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        
        p_ancestors = [node for node in self.find_node(root, p)[0]]
        q_ancestors = [node for node in self.find_node(root, q)[0]]
        #print(f"p ancestors {[node.val for node in self.find_node(root, p)[0]]}")
        #print(f"q ancestors {[node.val for node in self.find_node(root, q)[0]]}")


        shorter_list = p_ancestors if len(p_ancestors) < len(q_ancestors) else q_ancestors

        for i in range(len(shorter_list) - 1, - 1, -1):
            #print(f"shorter list element: {shorter_list[i].val}")
            #print(p_ancestors[i].val, q_ancestors[i].val)
            if p_ancestors[i] == q_ancestors[i]:
                return p_ancestors[i]
        return self.find_node(root, p)[1]
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            # if both the nodes are greater than the current node (no split) move to the right
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # if both nodes are less than the current node, move to the left, no split

            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left 
            # now the nodes have to split as one is greater or equal to it and the other is less than it 
            else:
                return curr


    def find_node(self, root, node, ancestors = None):
        
        if ancestors is None:
            ancestors = []
        if not root:  
            return None
        ancestors.append(root)
        if root.val == node.val:
            return ancestors, root
        
        if node.val > root.val:
            return self.find_node(root.right, node, ancestors)  
        else:
            return self.find_node(root.left, node, ancestors)   
        
# Helper functions for testing
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

def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)

# Test cases
def test():
    solution = Solution()
    
    # Test case 1
    root1 = build_tree([6,2,8,0,4,7,9,None,None,3,5])
    p1 = find_node(root1, 2)
    q1 = find_node(root1, 8)
    result1 = solution.lowestCommonAncestor(root1, p1, q1)
    print(f"Test 1: Expected 6, Got {result1.val if result1 else None}")
    
    # Test case 2
    root2 = build_tree([6,2,8,0,4,7,9,None,None,3,5])
    p2 = find_node(root2, 2)
    q2 = find_node(root2, 4)
    result2 = solution.lowestCommonAncestor(root2, p2, q2)
    print(f"Test 2: Expected 2, Got {result2.val if result2 else None}")

if __name__ == "__main__":
    test()