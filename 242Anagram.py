def anagram(s, t):
    sCounter = {}
    for letter in s:
        if letter in sCounter: # instead of using this if statement, you can do  tCounter[letter] = 1 + countS.get(letter, 0)
            sCounter[letter] += 1
        else:
            sCounter[letter] = 0
        tCounter = {}
    for letter in t:
        if letter in tCounter:
            tCounter[letter] += 1
        else:
            tCounter[letter] = 0
    return sCounter == tCounter

print(anagram("anagram", "nagaram"))