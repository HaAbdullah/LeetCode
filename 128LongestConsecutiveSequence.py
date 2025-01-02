def longestConsecutive(nums):
    nums.sort(reverse=True)
    count = 0 
    seen = set()
    for n in nums:
        c = 0
        while n + c + 1 in seen:
            c = c + 1
        if c > count:
            count = c 
        seen.add(n)
    if len(nums) > 1 and nums.count(nums[0]) == len(nums):
        return 1
    else:
        return count + 1 if nums else 0

# Updated test cases
print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(longestConsecutive([]))
print(longestConsecutive([0,0]))
