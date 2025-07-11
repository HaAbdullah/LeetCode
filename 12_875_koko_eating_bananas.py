import math

def minEatingSpeed(piles, h):
    # Set pointers L, R for possible values
    # Do binary search through possible values, adjusting them until you find the right one

    L = 1
    R = max(piles) 


    while L <= R:
        current_k = (R + L) // 2 


        calc_h = 0

        for pile in piles:
            calc_h += math.ceil(pile/current_k)
        print(f"current_k {current_k} makes calc_h {calc_h}")
        if calc_h > h:
            L = current_k + 1 
        elif calc_h  < h:
            R = current_k - 1
        else:
            return current_k

def minEatingSpeed(piles, h):
    L = 1
    R = max(piles)
    result = R  # Initialize with worst case
    
    while L <= R:
        current_k = (R + L) // 2
        
        calc_h = 0
        for pile in piles:
            calc_h += math.ceil(pile/current_k)
        
        print(f"current_k {current_k} makes calc_h {calc_h}")
        
        if calc_h <= h:  # Can finish in time or exactly on time
            result = current_k  # This is a valid answer
            R = current_k - 1   # Try to find a smaller valid speed
        else:  # Too slow
            L = current_k + 1   # Need a faster speed
    
    return result

# print(minEatingSpeed(piles = [3,6,7,11], h = 8))
# print(minEatingSpeed(piles = [30,11,23,4,20], h = 5))
print(minEatingSpeed(piles = [312884470], h = 312884469))