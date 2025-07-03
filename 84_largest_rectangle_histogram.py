def largestRectangleArea(heights):
    maxArea = 0
    stack = []
    for height in heights:
        num_pops = 0
        min_value = 0
        current_area = 0
        if len(stack) != 0 and height < stack[-1]:
            big_steppa = stack[-1]
            while len(stack) != 0 and height < stack[-1]:
                min_value = min(stack.pop(), min_value)
                num_pops += 1
            current_area = max(num_pops * min_value, big_steppa)
        else: 
                
                
                