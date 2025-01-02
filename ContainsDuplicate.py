def containsDuplicate(myList):
    return not(len(myList) == len(set(myList)))

print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))