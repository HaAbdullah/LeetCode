def romanToInteger(s):
    convert = {
        "I": 1,
        "V": 5, 
        "X": 10, 
        "L": 50, 
        "C": 100,
        "D": 500,
        "M": 1000
        }
    Integer = 0;
    index = 0
    while index < len(s):
        print(f"index:{index}")
        if index < (len(s) - 1):
            if s[index] == "I" and s[index+1] == "V":
                Integer += 4
                index+= 2
                continue
            elif s[index] == "I" and s[index+1] == "X":
                Integer += 9
                index+= 2
                continue
            elif s[index] == "X" and s[index+1] == "L":
                Integer += 40
                index+= 2
                continue
            elif s[index] == "X" and s[index+1] == "C":
                Integer += 90
                index+= 2
                continue
            elif s[index] == "C" and s[index+1] == "D":
                Integer += 400
                index+= 2
                continue
            elif s[index] == "C" and s[index+1] == "M":
                Integer += 900
                index+= 2
                continue                       
        Integer += convert[s[index]]
        print(Integer)
        index += 1
    return Integer

print(romanToInteger("III"))
#print(romanToInteger("LVIII"))
#print(romanToInteger("MCMXCIV"))