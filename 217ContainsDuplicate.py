# Solution 1: check if length of array == length of set
# Solution 2: nested for loop for every element checking if each element is present in the rest of the list (could use "in" for faster loop)
# Solution 3: Sort first and then check if sets of 2 elements are equal to each other
# Solution 4: Add each element to a set, if the element is already in the set return false, otherwise add it to it


def containsDuplicate(nums):
    #return len(set(nums)) != len(nums)
    
    # for i in range(len(nums)):
    #     currentNum = nums[i]
    #     for j in nums[i+1:]:
    #         if currentNum == j:
    #             return True
    # return False
    
    # nums.sort()
    # for i in range(len(nums)-1):
    #     if nums[i] == nums[i+1]:
    #         return True
    # return False
    
    myNums = set()
    
    for i in nums:
        if i in myNums:
            return True
        else:
            myNums.add(i)
    return False
        


nums = [1,3,2,1]
print(containsDuplicate(nums))