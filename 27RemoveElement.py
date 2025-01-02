def removeElement(nums, val):
    occurences = nums.count(val)
    size = len(nums)
    for i in range(occurences):
        nums.remove(val)
    print(nums)
    return size - occurences
    
print(removeElement([3,2,2,3], 3))
    