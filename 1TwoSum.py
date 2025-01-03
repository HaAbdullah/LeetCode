# def twoSum(nums, target):
#     seenNums = {}
#     for i in range(len(nums)):
#         wantedNum = target - nums[i]
#         if wantedNum in seenNums:
#             return [seenNums[wantedNum], i]
#         seenNums[nums[i]] = i


#Solution 1: nested loop checking if te needed number is present in the rest of the array
#Solution 2: WRONG CUZ ONCE U SORT INDEXES ARE MESSED UP. sort array, get pointer for left and right, if L + R too high, move R down 1, else move L up 1 keep going until you find smth
#Solution 3: loop through array adding each value to a dictionary along with its index, calculate the needed value and see if it is in the dictionary. If it is, return both indexes, otherwise, move on


def twoSum(nums, target):
    # for i in range(len(nums)):
    #     currentNumber = nums[i]
    #     neededNumber = target - currentNumber
    #     for j in range(i+1, len(nums)):
    #        if nums[j] == neededNumber:
    #             return [i, j]


    #WRONG    
    # nums.sort()
    # L = 0
    # R = len(nums) - 1
    
    # while (L < R):
    #     if ( nums[L] + nums[R] > target):
    #         R -= 1
    #     elif ( nums[L] + nums[R] < target):
    #         L += 1
    #     else:
    #         return [L, R]
    
    seen = {}
    for i in range(len(nums)):
        num = nums[i]
        needed = target - num
        if needed in seen:
            return [i, seen[needed]]
        else:
            seen[num] = i
        
        
        
    
        
# print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
# print(twoSum([3,3], 6))