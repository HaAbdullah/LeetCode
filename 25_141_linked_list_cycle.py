from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Helper function to create a linked list (with optional cycle)
def build_linked_list(values, pos=-1):
    """
    values: list of node values
    pos: index where tail connects (-1 means no cycle)
    """
    if not values:
        return None

    head = ListNode(values[0])
    curr = head
    nodes = [head]  # keep track of all nodes for cycle connection

    for val in values[1:]:
        new_node = ListNode(val)
        curr.next = new_node
        curr = new_node
        nodes.append(new_node)

    if pos != -1:
        curr.next = nodes[pos]  # create cycle

    return head

# Helper to print list (safe for no cycle only)
def print_linked_list(head, limit=20):
    count = 0
    res = []
    while head and count < limit:
        res.append(str(head.val))
        head = head.next
        count += 1
    if head:
        res.append("... (cycle detected in print)")
    print(" -> ".join(res) if res else "Empty List")

# Your solution class
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set_nodes = set()
        curr = head 
        while curr:
            if curr in set_nodes:
                return True 
            set_nodes.add(curr)
            curr = curr.next 
        return False

# ====== PLAYGROUND ======
# Example 1: No cycle
list1 = build_linked_list([3, 2, 0, -4], pos=-1)
print("List 1 (no cycle):")
print_linked_list(list1)

# Example 2: Cycle at position 1
list2 = build_linked_list([3, 2, 0, -4], pos=1)
print("\nList 2 (cycle at pos 1):")
print_linked_list(list2)  # will stop early if cycle exists

sol = Solution()
print("\nCheck for cycle:")
print("List 1:", sol.hasCycle(list1))  # Expected: False
print("List 2:", sol.hasCycle(list2))  # Expected: True
