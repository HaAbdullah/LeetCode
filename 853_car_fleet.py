def carFleet(target, position, speed):
    # [ (0,1),(3,3),(5,1),(8,4),(10,2)]
    # Create a stack of fleets
    # zip together position and speed in sorted decreasing position order
    # go through each tuple and calculate time to target, if its less the the head:
        # combine it witht he one and pop() .append() and keep doing that
    # return len(fleets)
    fleets = []
    cars = sorted(zip(position, speed), reverse = True)
    
    for position, speed in cars:
        time_to_target = (target - position) / speed
        if len(fleets) != 0 and time_to_target <= fleets[-1] :
            continue
        else:
            fleets.append(time_to_target)
            
    return len(fleets)
            
            


print(carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))