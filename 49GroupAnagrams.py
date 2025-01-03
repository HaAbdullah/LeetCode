# def groupAnagrams(strs):
#     WordCounter = {} # sortedWord : [words]
#     for word in strs:
#         sortedWord = ("".join((sorted(word))))
#         if sortedWord in WordCounter:
#             WordCounter[sortedWord].append(word)
#         else:
#             WordCounter[sortedWord] = [word]
#     return [group for group in WordCounter.values()]

#Solution 1: loop through array and create a sorted copy, add the original word to the dictionary with the key being the sorted copy

def groupAnagrams(strs):
    
    anagrams = {}
    for word in strs:
        newWord = "".join(sorted(word))
        anagrams[newWord] = anagrams.get(newWord, []) + [word]
        
    return list(anagrams.values())
        
    
print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
# print(groupAnagrams(strs = [""]))
# print(groupAnagrams(strs = ["a"]))