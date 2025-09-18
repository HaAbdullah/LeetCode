# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        # create a res variable
        res = []
        q = deque([root])
        # bfs sub function:
        while q:
            current_node = q.popleft()
            if current_node is not None:
                res.append(current_node)
                q.append(current_node.left)
                q.append(current_node.right)
            else:
                res.append("None")
        return ",".join(res)

    def deserialize(self, data):
        # split the res into a list 
        # create dequeue that is just the data
        # bfs through the dequue and create the res

        if not data: return None

        list_data = data.split(",")
        root = TreeNode(list_data[0])
        queue = deque([root])
        i = 1

        while queue and i < len(list_data):
            node = queue.popleft()

            #left child

            if list_data[i] != "None":
                node.left = TreeNode(int(list_data[i]))
                queue.append(node.left)
            i += 1 

            #right child
            
            if i < len(list_data) and list_data[i] != "None":
                node.right = TreeNode(int(list_data[i]))
                queue.append(node.right)
            i += 1 
        return root



# Test cases
def test():
    codec = Codec()
    
    # Test case 1: [1,2,3,null,null,4,5]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(5)
    
    serialized1 = codec.serialize(root1)
    deserialized1 = codec.deserialize(serialized1)
    print(f"Test 1 - Serialized: {serialized1}")
    
    # Test case 2: Empty tree
    serialized2 = codec.serialize(None)
    deserialized2 = codec.deserialize(serialized2)
    print(f"Test 2 - Serialized: {serialized2}")

# Helper function to print tree (for verification)
def print_tree(root):
    if not root:
        return "[]"
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")
    
    # Remove trailing nulls
    while result and result[-1] == "null":
        result.pop()
    
    return "[" + ",".join(result) + "]"

if __name__ == "__main__":
    test()