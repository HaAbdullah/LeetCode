from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]  # start with the empty subset
        for num in nums:
            new_subsets = []
            for curr in res:
                # create a new subset by adding num to the current subset
                new_subset = curr + [num]
                new_subsets.append(new_subset)
            # add all new subsets to the result
            res.extend(new_subsets)
        return res
