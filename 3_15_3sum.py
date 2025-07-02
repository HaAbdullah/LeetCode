def threeSum(nums):
    nums.sort()
    result = []

    for L in range(len(nums) - 2):
        if L > 0 and nums[L] == nums[L - 1]:
            continue  # Skip duplicates for L

        P = L + 1
        R = len(nums) - 1

        while P < R:
            total = nums[L] + nums[P] + nums[R]
            if total == 0:
                result.append([nums[L], nums[P], nums[R]])
                P += 1
                R -= 1
                # Skip duplicates for P and R
                while P < R and nums[P] == nums[P - 1]:
                    P += 1
                while P < R and nums[R] == nums[R + 1]:
                    R -= 1
            elif total < 0:
                P += 1
            else:
                R -= 1

    return result
print(threeSum([-1,0,1,2,-1,-4]))      # [[-1, -1, 2], [-1, 0, 1]]
print(threeSum([1,1,-2]))              # [[-2, 1, 1]]
print(threeSum([0,0,0,0]))             # [[0,0,0]]
print(threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))