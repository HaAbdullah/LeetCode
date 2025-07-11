# def characterReplacement(s, k):
#     L = 0 
#     R = 0 
#     longest_string = 0
#     replacements_left = k
#     character_indicies = {}
#     for i, c in enumerate(s):
#         if character_indicies.get(c, -1) == -1:
#             print("not yet in dictionary")
#         # if the last seen index of this character is less than the current window and there's no replacements
#         elif character_indicies[c] < L and replacements_left == 0:
#             longest_string = max(longest_string, R - L)
#             if character_indicies[c] >= i - k + 1:
#                 L = character_indicies[c]
#             else:
#                 L = i
#             replacements_left = k
#         else:
#             if c != s[L]:
#                 replacements_left -= 1 
            
#         character_indicies[c] = i
    
#         longest_string = max(longest_string, R - L)
#     return longest_string

# def characterReplacement(s, k):
#     L = 0 
#     R = 1
#     longest_string = 0
#     replacements_left = k

#     if len(s) == 0:
#         return 0
    
#     character_indicies = {s[L]: L}


#     for i, c in enumerate(s):
#         # if the current character is not the starting character of this substring and there's no replacements
#         #print(f"c: {c} s[L]: {s[L]} replacements_left{ {replacements_left}} L: {L} R: {i}")
#         if c != s[L] and replacements_left == 0:
#             #print("I got here")
#             longest_string = max(longest_string, i - L)
#             #check if the current character's last index is within the current character's index - replacements - 1 
#             if character_indicies.get(c, -100) >= i - k + 1:
#                 L = character_indicies[c]

#             # its too far, make the left pointer the current one
#             else:
#                 L = i
        
#         elif c != s[L] and replacements_left > 0:
#             #print("its not equal")
#             replacements_left -= 1
        
#         character_indicies[c] = i
#         longest_string = max(longest_string, i - L + 1)
#     return longest_string


def characterReplacement(s, k):
    # sliding window: can I add the next element without running out of replacements? yes: add it no: move L until you can 

    # Can i add the next element wi^thout running out of replacement = length_of_window - max_count < k 
    longest_string = 0
    max_count = 0
    counts = {}
    L = 0
    for R, c in enumerate(s):
        counts[c] = counts.get(c, 0) + 1
        max_count = max(max_count, counts[c])
        length_of_window = R - L + 1
        
        #if replacements needed > replacements we have
        if (length_of_window - max_count ) > k:
            counts[s[L]] -= 1
            L += 1

        longest_string = max(longest_string, R - L + 1)
    return longest_string


print(characterReplacement("ABAB", 2))
print(characterReplacement("AABAABBA", 1))
print(characterReplacement("AAAB", 0))
print(characterReplacement("ABBB", 2))

# AABABBA , k = 1 
# AABA = 4
# is last b (2) within 1 + 1 of current b (4)? yes, so L = last_b 
# last_b >= current_b - 1 + 1
# AABAABBA, k = 1 
# AABAA = 5
# is last b (2) within 1 + 1 of current b (5)?  no, L = new_b

# AABAABBA, k = 2
# AABAA = 5
# is last_b (2) within 2 + 1 of current b (5)? yes, L = last_b 

# AABAABBA
# L = 0, R = 5
# replacements left = 0 
# current dictionary = {A: 4, B: 2}