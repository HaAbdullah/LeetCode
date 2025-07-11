# def lengthOfLongestSubstring(s):
#     #max_length = 0 
#     # L = 0, R = 0 
#     # while R < len(s): we keep moving R forward and adding it to a set
#         # if we encounter an element already in the set, max_length = max(max_length, R - L - 1)
#         # move L until it reaches that element + 1 

#     current_characters = {}
#     max_length = 0
#     L , R = 0 , 0

#     while R < len(s):
#         if current_characters.get(s[R], -1) == -1:
#             current_characters[s[R]] = R
#         else:
#             print(f"current substring: {current_characters}")
#             max_length = max(max_length, (R - L))
#             while s[L] != s[R]:
#                 print(f"{s[L]} != s{[R]}")
#                 current_characters[s[L]] = -1 
#                 L += 1 
#             L += 1

#         R += 1
#     max_length = max(max_length, (R - L))
#     return max_length


def lengthOfLongestSubstring(s):
    # sliding window, can i add this next element wihtout it being a duplicate? yes: add it no: move L to current + 1 
    current_characters = {}
    max_length = 0
    L , R = 0 , 0

    while R < len(s):
        current_c = s[R]
        if current_c in current_characters and current_characters[current_c] >= L:
            L = current_characters[current_c] + 1

        max_length = max(max_length, (R - L + 1))
        current_characters[current_c] = R
        R += 1

    return max_length

print(lengthOfLongestSubstring("tmmzuxt"))
print(lengthOfLongestSubstring("dvdf"))

# print(lengthOfLongestSubstring(" "))