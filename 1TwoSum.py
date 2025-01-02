def twoSum(nums, target):
    seenNums = {}
    for i in range(len(nums)):
        wantedNum = target - nums[i]
        if wantedNum in seenNums:
            return [seenNums[wantedNum], i]
        seenNums[nums[i]] = i
print(twoSum([2,7,11,15], 9))
