def searchMatrix(matrix, target):
    # have L M R indicies that keep going until you move to one array
    # have l m r indicies that keep going until you move to one element
    
    L = 0
    R = len(matrix)
    M = 0
    
    while L < R:
        M = (R + L) // 2
        print(f"R: {R} L {L} M: {M}")
        MID = matrix[M]
        
        if MID[0] > target:
            print(f"{R} = {M} - 1")
            R = M 
        elif MID[len(MID) - 1] < target:
            print("ok wth")
            L = M + 1
        else:
            print(f"got here: {MID}")
            l = 0 
            r = len(MID) - 1
            mid = 0
            
            while l <= r:
                mid = (l + r) // 2
                if MID[mid] < target:
                    l = mid + 1
                elif MID[mid] > target:
                    r = mid - 1
                else:
                    return True
            return False
        
        
print(searchMatrix(matrix = [[1]], target = 1))               
# print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))            
# print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))