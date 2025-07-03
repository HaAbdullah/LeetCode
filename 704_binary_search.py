def search(nums, target):
    L = 0
    R = len(nums) - 1
    mid = 0
    while L <= R:
        mid = R + L // 2
        num=nums[mid]
        if num < target:
            L = mid + 1 
        elif num > target:
            R = mid - 1
        else:
            return mid
    return -1

print(search(nums = [-1,0,3,5,9,12], target = 9))