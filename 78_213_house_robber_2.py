# [1 [2 3] 1]

def rob(nums):
    if not nums: return 0 
    if len(nums) == 1: 
        return nums[0] 
    def robSection(nums):
        if not nums: return 0 
        if len(nums) == 1: return nums[0] 
        current_house_1 = nums[0] 
        current_house_2 = max(nums[0], nums[1])
        i = 2 
        while i < len(nums):
            new_house = max(nums[i] + current_house_1, current_house_2)
            print(current_house_1, current_house_2, new_house)
            current_house_1  = current_house_2
            current_house_2 = new_house
            i += 1 
        print(current_house_2)
        return current_house_2
    

    return max(robSection(nums[:-1]), robSection(nums[1:]))
print(rob([2,3,2]))
print(rob([1,2,3,1]))
print(rob([1]))
# 1 2 4 4 