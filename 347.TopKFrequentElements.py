'''
ATTEMPT 1:
def topKFrequent(nums,k):
    setNums = set(nums)
    counter = {}
    for num in setNums:
        counter[num] = nums.count(num)
    res = []
    for i in range(k):
        key_list = list(counter.keys())
        val_list = list(counter.values())  
        biggest = max(val_list)
        position = val_list.index(biggest)
        res.append(key_list[position])
        del counter[key_list[position]]
    return res
'''
from collections import defaultdict


def topKFrequent(nums,k):
    freq = [[] for i in range(len(nums)+1)]
    setNum = set(nums)
    for i in range(len(setNum)):
        freq[nums.count(list(setNum)[i])].append(list(setNum)[i])
    print(freq)
    res = []
    for i in range(len(freq) -1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
print(topKFrequent([1,1,1,2,2,3],2))

#print(topKFrequent([4,1,-1,2,-1,2,3],2))

#print(topKFrequent([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6],10))