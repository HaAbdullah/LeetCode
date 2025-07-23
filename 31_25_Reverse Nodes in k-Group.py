from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next

    def __str__(self):
        result = []
        node = self
        while node:
            result.append(str(node.val))
            node = node.next
        return " -> ".join(result)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # res = Node()
        # while curr:
            # reversals = 0 
            # curr_list = []
            # curr_in
            # while reversals < k:
                # if we reach null, just append the curr to the res and return res
                # reverse this next node, adding it to the curr_list
                # res.next = curr_list 
                # curr = curr.next 
            # curr = curr_inner 
        # return res.next
        
        res = ListNode(0)
        res_builder = res 
        
        curr = head
        
        while curr:
            group_start = curr  
            curr_inner = curr
            reversals = 0 

            prev = None 
            
            
            while reversals < k:
                if not curr_inner: 
                    res_builder.next = curr
                    return res.next
                # Create NEW node instead of modifying existing
                new_node = ListNode(curr_inner.val)
                new_node.next = prev
                prev = new_node
                curr_inner = curr_inner.next
                reversals += 1

            res_builder.next = prev  # Not reversed_list_head
            # move res_builder to last node of newly added reversed list
            while res_builder.next:
                res_builder = res_builder.next
            curr = curr_inner
            
            
        return res.next
def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])
    k = 3
    result = Solution().reverseKGroup(head, k)
    if result:
        print(result)
    else:
        print("Empty list")
