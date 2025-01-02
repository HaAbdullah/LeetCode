def longestCommonPrefix(strs):
    if "" in strs:
        return ""
    largestWord = ""
    for word in strs:
        if len(word) > len(largestWord):
            largestWord = word
    prefix = ""
    for letter in largestWord:
        prefix += letter
        for word in strs:
            if prefix != word[0:len(prefix)]:
                return prefix[0:-1]
    return prefix
                

strs = ["flower","flow","flight"]


print(longestCommonPrefix(strs))
  