# def maxSlidingWindow(nums, k):
    
    # L = 0
    # R = k - 1
    # Iterate until R = len(nums) - 1, moving L and R once each time
        # check max between nums[L:R+1] and add it to res
    # return res
    
    # L = 0 
    # R = k - 1
    # res = []
    # while R < len(nums):
    #     res.append(max(nums[L:R+1]))
    #     R += 1
    #     L += 1 
    # return res
    
    
# def maxSlidingWindow(nums, k):
#     if k == 1: return nums
#     L = 0
#     real_L = 0
#     R = k - 1
#     res = []
#     while R < len(nums):
#         print(f"current window: {nums[L:R+1]}")
#         window = nums[L:R+1]
#         max_val, rel_idx = max((val, idx) for idx, val in enumerate(window))
#         max_idx = L + rel_idx
#         print(max_val)
#         res.append(max_val)
#         if max_idx == real_L:
#             L += 1
#         else: 
#             # print(f"before: {nums[max_idx]}")
#             # nums[L] = max_val  # unnecessary mutation, can be removed
#             L = max_idx
#             # print(f"after: {nums[max_idx]}")
#         R += 1
#         real_L += 1
#     return res

from collections import deque 
def maxSlidingWindow(nums, k):
    # dequeue = dequeue
    # res = []
    # L and R pointers = 0
    # loop through nums
    # when R+1 - L > k: remove from front of dequeue if its index is less than L (outside of the window) and L+= 1
    # while nums[R] is greater than the front of the dequeue, keep removing elements 
    # add nums[R]
    # add dequeue[0] to res 
    # return res 
    
    de = deque()
    res = []
    L = 0
    canAdd = False
    for R, num in enumerate(nums):
        if (R + 1 - L) == k: 
            print(f"distance between two elements is {(R + 1 - L)}")
            if de and de[0][0] < L : de.popleft()
            L += 1
            canAdd = True
        while len(de) > 0 and num > de[-1][1]: de.pop()
        de.append((R, num))
        if canAdd:
            res.append(de[0][1])

    return res 

#optimal solution:
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = deque()  # Store indices only
        result = []
        
        for i in range(len(nums)):
            # Remove indices that are out of current window
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # Remove indices whose values are smaller than current
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            
            dq.append(i)
            
            # Add to result once we have a full window
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result


# print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
# print(maxSlidingWindow([1], 1))
#print(maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4))
# print(maxSlidingWindow([1,3,1,2,0,5], 3))
print(maxSlidingWindow([1,-1], 1))
# | 1 3 -1 | -3 5 3 6 7 : 3 
# |3 -3| 5 3 6 7 : 3 3 
# |-3 5 | 3 6 7 : 3 3 5
# | 5 3 | 6 7 : 3 3 5 5
# | 3 6 | 7 : 3 3 5 5 6
# | 6 7 | : 3 3 5 5 6 7 