def trap(height):
    L = 0
    R = L + 2
    total = 0
    sums = []

    while R < len(height):
        existsGreater = any(i >= height[L] for i in height[L + 1:])
        
        if not existsGreater:
            print(f"SKIPPING L: {L}")
            L = L + 1
            R = L + 2

        print(height[L], height[R])
        currentSum = min(height[L], height[R]) * (R - L - 1)
        sums.append(currentSum)

        if height[R] > height[L]:
            L = R
            R = L + 2
            total += sums[-1] - sum(sums[:-1])
            sums = []
        else:
            L = L + 1
            R = L + 2
            total += sums[-1] - sum(sums[:-1])
            sums = []

    return total

# Test case
print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
