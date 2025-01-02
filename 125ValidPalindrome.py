def isPalindrome(s):
    newString = ""
    s = s.lower()
    for i in range(len(s)):
        if s[i].isalnum():
            newString += s[i]
    return newString == newString[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))