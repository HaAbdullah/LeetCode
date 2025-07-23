# def trap(height):
#     if not height or len(height) < 3:
#         return 0
    
#     n = len(height)
#     res = 0
#     i = 0
    
#     while i < n - 1:
#         if height[i] == 0:
#             i += 1
#             continue
            
#         # Find next wall >= current height
#         j = i + 1
#         while j < n and height[j] < height[i]:
#             j += 1
        
#         if j < n:  # Found wall >= height[i]
#             # Add water between i and j
#             for k in range(i + 1, j):
#                 res += height[i] - height[k]
#             i = j
#         else:  # No wall >= height[i], find tallest in remaining
#             maxHeight = 0
#             maxIdx = i + 1
#             for k in range(i + 1, n):
#                 if height[k] > maxHeight:
#                     maxHeight = height[k]
#                     maxIdx = k
            
#             # Add water between i and maxIdx
#             for k in range(i + 1, maxIdx):
#                 res += maxHeight - height[k]
#             i = maxIdx
    
#     return res


def trap(height):
    res = 0
    
    # create left max
    current_left_max = 0
    left_max = []
    for h in height:
        left_max.append(current_left_max)
        current_left_max = h if h > current_left_max else current_left_max
    
    # create right max: must traverse in reverse order since its built from right side
    current_right_max = 0
    right_max = []
    
    for i in range(len(height) - 1, -1, -1):
        h = height[i]
        right_max.append(current_right_max)
        current_right_max = h if h > current_right_max else current_right_max
    # loop through array and calculate formula for each block, if the calc > 0, add it to the res 
    
    for i in range(len(height)):
        c_right_max = right_max[len(height) - 1 - i]
        c_left_max = left_max[i]
        c_height = height[i]
        
        c_water = min(c_right_max, c_left_max) - c_height
        if c_water > 0: 
            res += c_water
    
    return res

# Test cases
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Should be 6
# print(trap([4,2,0,3,2,5]))               # Should be 9  
# print(trap([4,2,3]))                     # Should be 1
# print(trap([5,4,1,2]))                   # Should 