def carFleet(target, position, speed):
    
    combined = []
    for i, pos in enumerate(position):
        combined.append((pos, speed[i]))

    # Sort by position in DESCENDING order (closest to target first)
    combined.sort(key= lambda x: x[0], reverse=True)
    print(f"Cars sorted by position (closest to target first): {combined}")

    stack = []

    for pos, spd in combined:
        print(f"\nProcessing car at position {pos} with speed {spd}")
        
        # Check if this car will be caught by any faster car behind it
        will_be_caught = False
        
        # Check against all cars already in stack (these are cars closer to target)
        for stack_pos, stack_spd in stack:
            if spd > stack_spd:  # This car is faster than a car ahead
                print(f"Checking if car at {pos} (speed {spd}) catches car at {stack_pos} (speed {stack_spd})")
                
                # Simulate second by second
                temp_pos = pos
                temp_stack_pos = stack_pos
                second = 0
                
                while temp_pos < target and temp_stack_pos < target and temp_pos < temp_stack_pos:
                    temp_pos += spd
                    temp_stack_pos += stack_spd
                    second += 1
                    
                    if temp_pos >= temp_stack_pos:  # This car catches up
                        print(f"Car at {pos} catches up to car at {stack_pos} at second {second}")
                        will_be_caught = True
                        break
                    
                    # Safety break
                    if second > 1000:
                        break
                        
                if will_be_caught:
                    break
        
        if not will_be_caught:
            stack.append((pos, spd))
            print(f"Car at {pos} forms its own fleet")
        else:
            print(f"Car at {pos} joins existing fleet")

    return stack, len(stack)
    
print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))