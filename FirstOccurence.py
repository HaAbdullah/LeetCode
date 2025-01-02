def strStr(haystack, needle):
    for i in range(len(haystack) + 1 - len(needle)):
        counter = 0
        for n in range(len(needle)):
            if haystack[i + n] == needle[n]: 
                counter += 1
            else:
                break 
            if counter == len(needle):  
                return i

    return -1
    
print(strStr("sadbutsad", "sad"))