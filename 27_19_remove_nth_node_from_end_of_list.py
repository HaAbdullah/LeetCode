from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    """Helper function to create a linked list from a Python list"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def print_linked_list(head):
    """Helper function to print a linked list"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int):

        # get the length of the list 
        curr = head 
        length = 0 
        while curr:
            length += 1
            curr = curr.next

        # find index we need to remove 
        index = length - n 

        # loop through list with prev, curr, next and find index and connect prev to next 
        prev = None
        curr = head 
        
        i = 0


        while i != index:
            prev = curr
            curr = curr.next
            i += 1
        if index == 0:
            return head.next
        else:
            prev.next = curr.next
        return head 
#Test your solution
solution = Solution()
head = create_linked_list([1, 2, 3, 4, 5])
result = solution.removeNthFromEnd(head, 2)
print(print_linked_list(result))  # Should print [1, 2, 3, 5]

head = create_linked_list([1])
result = solution.removeNthFromEnd(head, 1)
print(print_linked_list(result))  # Should print [1, 2, 3, 5]
# solution = Solution()
# head = create_linked_list([1, 2, 3, 4, 5])
# result = solution.removeNthFromEnd(head, 2)
# print(result) 