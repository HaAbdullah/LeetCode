# def trap(height):
# ATTEMPT 1: WORKS FOR 2ND TEST CASE 
#     L = 0
#     R = len(height) - 1
#     water = 0
#     while L < R: 
#         water += min(height[L], height[R]) * R - L
#         L += 1
#         R -= 1
#         print(water)
#         water -= height[L]
#         water -= height[R]
#     return water 
    
    
def trap(height):
    L = 0
    R =  L + 1
    total = 0
    currentSum = 0
    sums = []
    while (R < len(height)):
        existsGreater = False
        for i in height[L+1:]:
            if i >= height[L]:
                existsGreater = True
        if not existsGreater:
            print(f"SKIPPING L: {L}")
            L = L + 1
            R = L + 1
            
        print(height[L], height[R])
        # print(f"distance = {R - L - 1}")
        # print(f"lowest height: {min(height[L], height[R])}")
        currentSum = min(height[L], height[R]) * (R - L - 1)
        between = 0
        sums.append(currentSum)
        if height[R] > height[L]:
            L = R
            R = L + 1
            
            total += sum(sums) - between
            sums = []
        else:
            R = R + 1
        print(f"CURRENTSUM: {currentSum}")
    return total
        
        
        
#print(trap([4,2,0,3,2,5]))
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))