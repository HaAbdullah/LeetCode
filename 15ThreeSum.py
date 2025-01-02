def threeSum(nums):
    r = []
    allCounters = {}
    for i in range(len(nums)):
        currentNums = set()
        target = -(nums[i])
        for j in range(i+1, len(nums)):
            #print(f"START: {nums[i]} currentNums: {currentNums}")
            wanted2 = target - nums[j]
            if wanted2 in currentNums:
                r.append([nums[i], wanted2, nums[j]])
                print("ADDED")
                allCounters[j] = {nums[i] wanted2, nums[j]}
            else:
                currentNums.add(nums[j])
            print(allCounters)
    return r
print(threeSum([-1,0,1,2,-1,-4]))