def trap(height):
    if not height or len(height) < 3:
        return 0
    
    n = len(height)
    res = 0
    i = 0
    
    while i < n - 1:
        if height[i] == 0:
            i += 1
            continue
            
        # Find next wall >= current height
        j = i + 1
        while j < n and height[j] < height[i]:
            j += 1
        
        if j < n:  # Found wall >= height[i]
            # Add water between i and j
            for k in range(i + 1, j):
                res += height[i] - height[k]
            i = j
        else:  # No wall >= height[i], find tallest in remaining
            maxHeight = 0
            maxIdx = i + 1
            for k in range(i + 1, n):
                if height[k] > maxHeight:
                    maxHeight = height[k]
                    maxIdx = k
            
            # Add water between i and maxIdx
            for k in range(i + 1, maxIdx):
                res += maxHeight - height[k]
            i = maxIdx
    
    return res

# Test cases
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Should be 6
print(trap([4,2,0,3,2,5]))               # Should be 9  
print(trap([4,2,3]))                     # Should be 1
print(trap([5,4,1,2]))                   # Should be 1