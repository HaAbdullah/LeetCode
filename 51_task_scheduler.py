from collections import Counter, deque
import heapq

def task_scheduler(tasks, n):
    """
    Schedule tasks with cooldown period n between same tasks.
    Returns total time units needed.
    """
    if not tasks:
        return 0
    
    # Count frequency of each task
    task_counts = Counter(tasks)
    
    # Max heap for task frequencies (use negative for max heap)
    max_heap = [-count for count in task_counts.values()]
    heapq.heapify(max_heap)
    
    # Queue to store tasks in cooldown: (time_available, frequency)
    cooldown_queue = deque()
    
    time = 0
    
    while max_heap or cooldown_queue:
        time += 1
        
        # Check if any task in cooldown is ready
        if cooldown_queue and cooldown_queue[0][0] == time:
            _, freq = cooldown_queue.popleft()
            heapq.heappush(max_heap, freq)
        
        if max_heap:
            # Execute the most frequent task
            freq = heapq.heappop(max_heap)
            
            # If task has remaining executions, put it in cooldown
            if freq < -1:  # Remember we're using negative values
                cooldown_queue.append((time + n + 1, freq + 1))
        
        # If no task available, we're idle (this happens automatically)
    
    return time

# Alternative approach - your style but fixed:
def task_scheduler_fixed(tasks, n):
    """
    Fixed version of your approach
    """
    if not tasks:
        return 0
        
    tasks_dict = Counter(tasks)
    res = 0
    my_heap = []
    
    # Queue stores (time_ready, elem, count)
    queue = deque()
    
    # Initialize all tasks as ready at time 0
    for elem, count in tasks_dict.items():
        heapq.heappush(my_heap, (-count, elem))
    
    while my_heap or queue:
        res += 1  # Increment time
        
        # Move ready tasks from queue to heap
        while queue and queue[0][0] <= res:
            _, elem, count = queue.popleft()
            heapq.heappush(my_heap, (-count, elem))
        
        if my_heap:
            # Execute most frequent task
            neg_count, elem = heapq.heappop(my_heap)
            count = -neg_count
            print(f"Time {res}: Execute {elem}")
            
            # If task has more executions, add to cooldown queue
            if count > 1:
                ready_time = res + n + 1  # Ready after cooldown
                queue.append((ready_time, elem, count - 1))
        else:
            print(f"Time {res}: IDLE")
    
    return res

# Test cases
if __name__ == "__main__":
    # Test case 1
    tasks1 = ["A", "A", "A", "B", "B", "B"]
    n1 = 2
    print(f"Tasks: {tasks1}, n={n1}")
    result1 = task_scheduler_fixed(tasks1, n1)
    print(f"Total time: {result1}")
    print()
    
    # Test case 2  
    tasks2 = ["A", "A", "A", "B", "B", "B"]
    n2 = 0
    print(f"Tasks: {tasks2}, n={n2}")
    result2 = task_scheduler_fixed(tasks2, n2)
    print(f"Total time: {result2}")
    print()
    
    # Test case 3
    tasks3 = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n3 = 2
    print(f"Tasks: {tasks3}, n={n3}")
    result3 = task_scheduler_fixed(tasks3, n3)
    print(f"Total time: {result3}")