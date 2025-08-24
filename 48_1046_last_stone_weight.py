import heapq
from typing import List


def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        
        # until there's only 1 rock 
        while len(stones) > 1:
            print(stones)
        # pop largest two rocks 
            largest = -heapq.heappop(stones)
            sndlargest = -heapq.heappop(stones)
        # largest - smallest
            res = largest - sndlargest
            if res != 0: heapq.heappush(stones, -res)
        # if res != 0, add it to the heap 
        
        return -stones[0] if stones else 0


print(lastStoneWeight([2,7,4,1,8,1]))
        