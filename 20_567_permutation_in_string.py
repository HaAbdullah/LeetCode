def checkInclusion(s1, s2):
    # sliding window: can I add the next character in S2 without getting out of S1's restraints? yes: add it, no: move L until it does

    #can i add the next character in S2 without getting out of S1's restraints? means if i add the character, is it still < s1_count[c]

    # OPTIMIZATION: fix sized window!
    res = False
    s1_count = {}
    for i in s1:   
        s1_count[i] = s1_count.get(i, 0) + 1

    L = 0
    s2_window_count = {}
    for R, c in enumerate(s2):
        s2_window_count[c] = s2_window_count.get(c, 0) + 1 

        # character is not in s1, move L to R

        if s1_count.get(c, -1000) == -1000:
            L = R + 1
            s2_window_count = {}
            continue
        
        # known character goes above limit
        #print(f"{s2_window_count[c]} for {c} > {s1_count.get(c, 0)}")
        while s2_window_count[c] > s1_count.get(c, 0):
            #print("doing the minus")
            s2_window_count[s2[L]] -= 1
            L += 1 
        print(s1_count, s2_window_count)

        # INCLUSION
        if R - L + 1 == len(s1):
            res = True
            for s in s1:
                if s1_count[s] != s2_window_count.get(s, 0):
                    res = False

        if res == True: return True
    
    return res

print(checkInclusion(s1 = "ab", s2 = "eidboaoo"))
print(checkInclusion(s1 = "ab", s2 = "eidbaooo"))