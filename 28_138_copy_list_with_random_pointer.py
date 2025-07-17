# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
    """
    Your solution goes here.
    
    Args:
        head: Node - The head of the original linked list
        
    Returns:
        Node - The head of the deep copied linked list
    """

    # create dictionary for {index, Node}
    old_to_new = {}
    # Loop through original list 
    curr_og = head
    new_head = Node(0)  
    curr_new = new_head
    i = 0
    while curr_og:
        # copy each value and normal pointer 
        new_node = Node(curr_og.val, None, None)
        curr_new.next = new_node
        # store index and Node 
        old_to_new[curr_og] = new_node
        i += 1
        curr_new = curr_new.next 
        curr_og = curr_og.next



    # loop through original list and new list at the same time 
    curr_og = head
    curr_new = new_head.next
    while curr_og:
        # for each original list's random pointer, search for that pointer's index in the dictionary and assign it 
        if curr_og.random:
            curr_new.random = old_to_new[curr_og.random]
        curr_new = curr_new.next 
        curr_og = curr_og.next
    # return head of the new list 
    return new_head.next

# Helper function to create a linked list from the input format
def create_linked_list(arr):
    """
    Creates a linked list from array format [[val, random_index], ...]
    """
    if not arr:
        return None
    
    # Create all nodes first
    nodes = []
    for i, (val, _) in enumerate(arr):
        nodes.append(Node(val))
    
    # Set up next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Set up random pointers
    for i, (_, random_idx) in enumerate(arr):
        if random_idx is not None:
            nodes[i].random = nodes[random_idx]
    
    return nodes[0]

# Helper function to convert linked list back to array format for testing
def linked_list_to_array(head):
    """
    Converts linked list back to array format for easy comparison
    """
    if not head:
        return []
    
    # First pass: collect all nodes and create index mapping
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    
    # Create node to index mapping
    node_to_index = {node: i for i, node in enumerate(nodes)}
    
    # Second pass: create result array
    result = []
    for node in nodes:
        random_idx = node_to_index[node.random] if node.random else None
        result.append([node.val, random_idx])
    
    return result

# Test cases
def test_copyRandomList():
    print("Testing Deep Copy Linked List with Random Pointer")
    print("=" * 50)
    
    # Test Case 1: Example from problem
    print("Test Case 1:")
    input1 = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    original1 = create_linked_list(input1)
    copied1 = copyRandomList(original1)
    result1 = linked_list_to_array(copied1)
    print(f"Input:    {input1}")
    print(f"Expected: {input1}")
    print(f"Got:      {result1}")
    print(f"Pass:     {result1 == input1}")
    
    # Check that it's actually a deep copy (different objects)
    if copied1:
        deep_copy_check = copied1 is not original1
        print(f"Deep copy check: {deep_copy_check}")
    print()
    
    # Test Case 2: Simple case
    print("Test Case 2:")
    input2 = [[1,1],[2,1]]
    original2 = create_linked_list(input2)
    copied2 = copyRandomList(original2)
    result2 = linked_list_to_array(copied2)
    print(f"Input:    {input2}")
    print(f"Expected: {input2}")
    print(f"Got:      {result2}")
    print(f"Pass:     {result2 == input2}")
    print()
    
    # Test Case 3: Empty list
    print("Test Case 3:")
    input3 = []
    original3 = create_linked_list(input3)
    copied3 = copyRandomList(original3)
    result3 = linked_list_to_array(copied3)
    print(f"Input:    {input3}")
    print(f"Expected: {input3}")
    print(f"Got:      {result3}")
    print(f"Pass:     {result3 == input3}")
    print()
    
    # Test Case 4: Single node
    print("Test Case 4:")
    input4 = [[1,None]]
    original4 = create_linked_list(input4)
    copied4 = copyRandomList(original4)
    result4 = linked_list_to_array(copied4)
    print(f"Input:    {input4}")
    print(f"Expected: {input4}")
    print(f"Got:      {result4}")
    print(f"Pass:     {result4 == input4}")
    print()
    
    # Test Case 5: All random pointers point to first node
    print("Test Case 5:")
    input5 = [[3,None],[3,0],[3,0]]
    original5 = create_linked_list(input5)
    copied5 = copyRandomList(original5)
    result5 = linked_list_to_array(copied5)
    print(f"Input:    {input5}")
    print(f"Expected: {input5}")
    print(f"Got:      {result5}")
    print(f"Pass:     {result5 == input5}")

# Run the tests
if __name__ == "__main__":
    test_copyRandomList()