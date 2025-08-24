import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.nums = nums 
        self.my_heap = nums 
        heapq.heapify(self.my_heap)
        
        while (len(self.my_heap)) > k:
            heapq.heappop(self.my_heap)

    def add(self, val: int) -> int:
        # we always add the val
        heapq.heappush(self.my_heap, val)
        if len(self.my_heap) > self.k:
            heapq.heappop(self.my_heap)
        # then we can check if the lenght is greater, if it is, pop
        
        return self.my_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)