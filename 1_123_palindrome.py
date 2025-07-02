def is_palindrome(s):
    s = s.lower()
    l, r = 0, len(s) - 1

    while l <= r:
        while l < len(s) and not s[l].isalnum():
            l += 1
        while r >= 0 and not s[r].isalnum():
            r -= 1

        # Safety check: only compare if both pointers are valid
        if l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

    return True


print(is_palindrome("."))

