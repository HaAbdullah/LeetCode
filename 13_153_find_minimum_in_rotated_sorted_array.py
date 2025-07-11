def findMin(nums):
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left + right) // 2         
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]+5


print(findMin([5,1,2,3,4]))


print(findMin([2,1]))