def findMedianSortedArrays(nums1, nums2):
    L1, L2 = 0
    R1 = len(nums1) - 1
    R2 = len(nums2) - 1

    # find the one with the larger medium 
    # check if larger's right > smaller's right
        # YES: move larger's right to middle 
        # NO: move smaller 