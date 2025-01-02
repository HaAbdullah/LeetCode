def groupAnagrams(strs):
    WordCounter = {} # sortedWord : [words]
    for word in strs:
        sortedWord = ("".join((sorted(word))))
        if sortedWord in WordCounter:
            WordCounter[sortedWord].append(word)
        else:
            WordCounter[sortedWord] = [word]
    return [group for group in WordCounter.values()]

print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))