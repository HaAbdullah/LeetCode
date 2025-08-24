from typing import Collection 
import heapq
import math
def kClosest(points, k):
    res = [] 
    heapq.heapify(res)
    for x,y in points:
        distance = math.sqrt(x * x + y * y)
        heapq.heappush(res, (-distance, [x,y]))
        if len(res) > k: heapq.heappop(res)
    return [y for x,y in list(res)]
        
        
        
print(kClosest([[1,3],[-2,2]], 1))