def maxProfit(prices):
    # MIN = prices(0)
    # MAX = prices[0]
    # l = 0, R = 0
    # while L < len(prices):
        # R+=1
        # if prices(R) > MAX:
            # MAX = prices(R)
        # if prices(R) < MIN:
            # MIN = prince(R)
            # L = R 
    greatest_difference = 0     
    L, R = 0, 0
    
    while R < len(prices):
        print(f"prices[R] : {R} {prices[R]} prices[L] {L}  : {prices[L]}")
        current_difference = (prices[R] - prices[L]) 
        greatest_difference = current_difference if current_difference > greatest_difference else greatest_difference
        if prices[R] < prices[L]:
            L = R

        R += 1
            
    return greatest_difference
        
        
print(maxProfit([7,1,5,3,6,4]))