# Brute forceish (n log n)
def findKthLargest(nums,k):
    return sorted(nums)[-k]

import heapq

# custom sort  ( k log n )
def findKthLargest(nums, k):
    # make nums in to a max heap 
    nums = [-x for x in nums]
    heapq.heapify(nums)
    # pop k times, kth pop is largest
    while k != 0:
        poppedElement = -heapq.heappop(nums)
        k -= 1 
    return poppedElement

# quick select ( average: O(n) worst case: O(n^2)
def findKthLargest(nums, k):
    k = len(nums) - k # convert k into the index we need

    def quickSelect(l, r):
        # select right most element as the pivot and create a pointer that you will be replacing and incrementing 
        pivot = nums[r]
        pointer = l
        # loop through the array ( from l to the pivot but not including it )
        for i in range(l, r):
            # if the current element is less than the pivot, swap the pointer element and current element 
            if nums[i] < pivot: 
                temp = nums[pointer]
                nums[pointer] = nums[i]
                nums[i] = temp 
                # incremement the pointer 
                pointer += 1 
        # once youve reached the end of the array, you can swap the current pointer with the pivot we chose 
        temp = nums[pointer]
        nums[pointer] = nums[r] # this means "pointer" now contains the pivot
        nums[r] = temp


        # now we have all the elements to the right of the pivot be greater than it and all the elements less than the pivot be on the left of it
        # now we can check if the pivot is the kth element and if its not, we can just sort the needed half 
        if pointer > k: 
            return quickSelect(l, pointer - 1)
        elif pointer < k:
            return quickSelect(pointer + 1, r)
        else: return nums[pointer]

    return quickSelect(0, len(nums) - 1)

print(findKthLargest(nums = [3,2,1,5,6,4], k = 2))
print(findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))