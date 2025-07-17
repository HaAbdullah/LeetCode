from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to create a linked list from a list of values
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res) if res else "Empty List")

# Your solution class
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2 
        res_head = ListNode()
        curr_res = res_head 
        res = []
        print(f"current head is : {res_head.val}")
        while curr1 and curr2:
            # find lower one, add it to the list, and then move head 

            if curr1.val < curr2.val:
                curr_res.next = curr1
                curr1 = curr1.next 
                curr_res = curr_res.next
            else:
                curr_res.next = curr2
                curr2 = curr2.next 
                curr_res = curr_res.next

        if curr1:
            curr_res.next = curr1
        if curr2:
            curr_res.next = curr2
                
        return res_head.next

# ====== PLAYGROUND ======

# Test inputs
list1_values = [1, 2, 4]
list2_values = [1, 3, 4]

list1 = build_linked_list(list1_values)
list2 = build_linked_list(list2_values)

print("List 1:")
print_linked_list(list1)

print("List 2:")
print_linked_list(list2)

# Run your merge function
sol = Solution()
merged_head = sol.mergeTwoLists(list1, list2)

print("\nMerged List:")
print_linked_list(merged_head)
