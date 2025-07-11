from collections import Counter

def minWindow(s, t):
    shortest_string = " " * 100
    count_t = Counter(t)
    count_s = {}
    L = 0
    required = len(count_t)
    formed = 0

    for R in range(len(s)):
        s_char = s[R]
        count_s[s_char] = count_s.get(s_char, 0) + 1

        # If this character matches t requirement, increase 'formed'
        if s_char in count_t and count_s[s_char] == count_t[s_char]:
            formed += 1

        # Try to shrink the window from the left while it's still valid
        while formed == required:
            window = s[L:R+1]
            if len(window) < len(shortest_string):
                shortest_string = window

            print(window)  # Optional: show valid windows

            left_char = s[L]
            count_s[left_char] -= 1
            if left_char in count_t and count_s[left_char] < count_t[left_char]:
                formed -= 1

            L += 1

    return shortest_string if shortest_string.strip() else ""


print(minWindow(s="ADOBECODEBANC", t="ABC"))
# print(minWindow(s="BAACAB", t="ABC"))