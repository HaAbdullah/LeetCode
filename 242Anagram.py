# def anagram(s, t):
#     sCounter = {}
#     for letter in s:
#         if letter in sCounter: # instead of using this if statement, you can do  tCounter[letter] = 1 + countS.get(letter, 0)
#             sCounter[letter] += 1
#         else:
#             sCounter[letter] = 0
#         tCounter = {}
#     for letter in t:
#         if letter in tCounter:
#             tCounter[letter] += 1
#         else:
#             tCounter[letter] = 0
#     return sCounter == tCounter

# Solution 1: Great hashmaps for both and count each letter then compare counts
# Solution 2: No extra memory needed: sort words and then loop through both at the same time checking if their characters are equal
def anagram(s, t):
    '''
    if len(s) != len(t), return false
    Loop through both strings and add each letter to dict1 and dict2 
    loop through dict1 and check if each key's value is equal to the same value in dict2, return false if not
    
    return true 
    '''
    if len(s) != len(t):
        return False
    dictS = {}
    dictT = {}
    for i in range(len(s)):
        charS = s[i]
        charT = t[i]
        if charS in dictS:
            dictS[charS]+= 1
        else:
            dictS[charS] = 1
            
        if charT in dictT:
            dictT[charT] += 1
        else:
            dictT[charT] = 1
            
    for char in dictS:
        if char not in dictT or dictT[char] != dictS[char]:
            return False
    return True
    

print(anagram("anagram", "nagaram"))
#print(anagram("rat", "car"))