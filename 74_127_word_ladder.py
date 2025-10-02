from collections import deque

def ladderLength(beginWord, endWord, wordList):
    def isConnected(word1, word2):
        count = 0 
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                  count += 1
        return count == len(word1) - 1

    if beginWord not in wordList:
        wordList.append(beginWord)
    adjList = {i: [] for i in wordList}
    #print("HELLO:", adjList)
    for i in range(len(wordList)):
        for j in range(i + 1, len(wordList)):
            if isConnected(wordList[i], wordList[j]):
                adjList[wordList[i]].append(wordList[j])
                adjList[wordList[j]].append(wordList[i])

    q = deque([beginWord])
    visited = set()
    res = 0 
    while q:
        res += 1
        for i in range(len(q)):
            word = q.popleft()
            visited.add(word)
            if word == endWord:
                return res 
            for neighbor in adjList[word]:
                if neighbor not in visited:
                    q.append(neighbor)
    return 0

    

from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord not in wordList:
            wordList.append(beginWord)

        L = len(beginWord)
        
        # Build mapping: generic pattern -> words
        patternMap = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                patternMap[pattern].append(word)
        
        # Build adjacency list using patternMap
        adjList = {word: [] for word in wordList}
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                for neighbor in patternMap[pattern]:
                    if neighbor != word:
                        adjList[word].append(neighbor)

        # BFS
        q = deque([beginWord])
        visited = set([beginWord])
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for neighbor in adjList[word]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        return 0


#print(ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))