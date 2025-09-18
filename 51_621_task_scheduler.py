from collections import deque
import heapq

def leastInterval(tasks, n):
    # we dont care about the letters them selves since its just the least interval that we're returning 
    # get all the counts of each task
    # create a max heap with the counts of each task 
    
    # create an empty queue
    # create a time variable
    # while either the queue or the max heap has elements:
        # increment the time
        # pop one element from the heap and subtract its count by one and then add it to the queue as (count, current_time + cooldown)
        # if the first element of the queue has a time of current_time, pop it and add it to the queue 
        # 
    # return time 

    counts = {}
    for task in tasks:
        counts[task] = 1 + counts.get(task, 0)

    counts_heap = [- task for task in counts.values()]
    heapq.heapify(counts_heap)

    q = deque([])
    current_time = 0
    while counts_heap or q:
        current_time += 1 

        # add current task to heap 
        if counts_heap: 
            popped_task = -heapq.heappop(counts_heap)
            popped_task -= 1 
            if popped_task != 0: 
                q.append((popped_task, current_time + n))
                

        # add any ready elements to the heap
        if q and q[0][1] == current_time:
            heapq.heappush(counts_heap, -q[0][0])
            q.popleft()
    return current_time
print(leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
# print(leastInterval(["A","C","A","B","D","B"], n = 1))
# print(leastInterval(tasks = ["A","A","A", "B","B","B"], n = 3))

