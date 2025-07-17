from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to create a linked list from a list
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
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values))

# Solution class with reverseList method (you can implement it here)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr 
            curr = next_temp 

        print(" -> ".join(res))
        return prev
    
    def lengthList(self, head: Optional[ListNode]) -> int:
        res = 0
        curr = head
        while curr:
            res += 1
            curr = curr.next
        return res
    
    def lengthList_recursive(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        else:
            return 1 + self.lengthList_recursive(head.next)
        

# ====== PLAYGROUND ======

# Create a sample linked list
values = [1, 2, 3, 4, 5]
head = build_linked_list(values)

print("Original linked list:")
print_linked_list(head)



# Reverse the linked list
sol = Solution()
reversed_head = sol.reverseList(head)

print("linked list length:")
print(sol.lengthList(reversed_head))

print("linked list recursive length:")
print(sol.lengthList(reversed_head))


print("\nReversed linked list:")
print_linked_list(reversed_head)
