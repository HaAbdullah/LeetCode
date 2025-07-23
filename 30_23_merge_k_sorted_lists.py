from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Utility to convert linked list to list (for easy output comparison)
    def to_list(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result

# Utility to convert a list to a linked list
def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Utility to convert a list of lists to a list of linked lists
def build_list_of_linked_lists(arrays):
    return [build_linked_list(arr) for arr in arrays]

class Solution:
    def to_list(node: Optional[ListNode]) -> List[int]:
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
    #     res = ListNode(0)
    #     current = res
    #     lists = [l for l in lists if l]
    #     # loop until there are non-empty lists
    #     while len(lists) > 0:
    #         smallest = float('inf')
    #         smallest_index = -1
    #         # loop through each list and find the smallest number and smallest node
    #         for i, list in enumerate(lists):
    #             if list and list.val < smallest:
    #                 smallest = list.val 
    #                 smallest_index = i
                    
    #         # add smallest node to result and move it forward 
    #         current.next = lists[smallest_index]
    #         current = current.next 
            
    #         lists[smallest_index] = lists[smallest_index].next
            
    #         if lists[smallest_index] == None:
    #             del lists[smallest_index]
                
    #         print(f"current: {Solution.to_list(res.next)}")  # ✅ fixed: use class name + res.next
    #     return res.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None 
        
        # go through 2 lists at a time and merge them adding them to the new version of lists 
        while len(lists) > 1:
            new_lists = []
            for i in range(0, len(lists), 2):
                list_1 = lists[i]
                list_2 = lists[i+1] if (i + 1) < len(lists) else None 
                
                # merge the two lists 
                merged_list = ListNode(0)
                curr_res = merged_list

                while list_1 and list_2:
                    if list_1.val < list_2.val:
                        curr_res.next = list_1
                        list_1 = list_1.next  
                        curr_res = curr_res.next 
                    else:
                        curr_res.next = list_2
                        curr_res = curr_res.next 
                        list_2 = list_2.next 
                
                if list_1:
                    curr_res.next = list_1 
                if list_2:
                    curr_res.next = list_2 
                    
                new_lists.append(merged_list.next)
                #print([Solution.to_list(node) for node in new_lists])
            lists = new_lists
        return lists[0]
            
            

                    
                

# ---- TEST CASES ----
test_inputs = [
    [[1, 4, 5], [1, 3, 4], [2, 6]]
]

expected_outputs = [
    [1, 1, 2, 3, 4, 4, 5, 6]
]

sol = Solution()

for i, test in enumerate(test_inputs):
    lists = build_list_of_linked_lists(test)
    result_head = sol.mergeKLists(lists)
    output = result_head.to_list() if result_head else []
    print(f"Test Case {i+1}: Output = {output}, Expected = {expected_outputs[i]}")
