def maxArea(height):
    L = 0
    R = len(height) - 1
    sum = 0 
    current_sum = -1
    while L < R:
        left = height[L]
        right = height[R]

        chosen = left if left < right else right 
        current_sum = chosen * (R - L)
        sum = current_sum if current_sum > sum else sum 

        if left < right:
            L += 1
        elif left > right:
            R -= 1
        else:
            if height[L + 1] > height[R - 1]:
                R -= 1
            elif height[L + 1] < height[ R - 1]:
                L += 1
            else:
                L += 1

    return sum


print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))
                
    