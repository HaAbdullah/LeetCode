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
def print_linked_list(head, limit=50):
    count = 0
    res = []
    while head and count < limit:
        res.append(str(head.val))
        head = head.next
        count += 1
    if head:
        res.append("... (possible cycle or very long list)")
    print(" -> ".join(res) if res else "Empty List")

# Your solution class
class Solution:

        


    # def reorderList(self, head: Optional[ListNode]):
    #     """
    #     Do not return anything, modify head in-place instead.
    #     """

        
    #     nodes = []
    #     curr = head

    #     while curr:
    #         nodes.append(curr.val)
    #         curr = curr.next

    #     L = 1 
    #     R = len(nodes) - 1

    #     new_dummy = head
    #     while L <= R:
    #         if L == R:
    #             new_dummy.next = ListNode(nodes[L])
    #         else:
    #             new_dummy.next = ListNode(nodes[R])
    #             new_dummy = new_dummy.next
    #             new_dummy.next = ListNode(nodes[L])
    #             new_dummy = new_dummy.next
    #         L += 1
    #         R -= 1


    def reorderList(self, head: Optional[ListNode]):
        # find half point
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next 
        
        mid = slow 
        
        # split left and right 
        left = head 
        right = mid.next 
        mid.next = None
                          
        # print("left half = ", end="")
        # print_linked_list(left)
        # print("right half = ", end="")
        # print_linked_list(right)

        # reverse right half 
        curr = right 
        prev = None 
        while curr:
            next_temp = curr.next
            curr.next = prev 
            prev = curr
            curr = next_temp 

        right = prev
        # print("right half reversed = ", end="")
        # print_linked_list(right)
        # loop through left and right and keep making them point to each other
        while left and right:
            right_temp = right.next
            left_temp = left.next

            left.next = right
            right.next = left_temp

            left = left_temp
            right = right_temp


# ====== PLAYGROUND ======
# Test case
values = [1, 2, 3, 4, 5]  # Expected reorder: 1 -> 5 -> 2 -> 4 -> 3
head = build_linked_list(values)

print("Original list:")
print_linked_list(head)

# Apply reorder
sol = Solution()
sol.reorderList(head)


print("\nReordered list:")
print_linked_list(head)
