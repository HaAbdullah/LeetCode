def findDuplicate(nums):
    # loop through a mock list: one that each mock[nums[i]] = mock[x + 1], this will make sure theres only 1 of each element
    # this is allowed because the range of the integer is [1, N]
    
    # loop through mock list using slow and fast pointers
    fast = nums[0]
    slow = nums[0]
    
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        # when slow and fast meet, break

        if slow == fast:
            break

    # put slow to the head and then keep incremementing slow and fast till they meet, thats the duplicate
    slow = nums[0]
    
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow 