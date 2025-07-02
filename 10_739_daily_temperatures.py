# # def dailyTemperatures(temperatures):
# #     # brute force
# #     res = []
# #     for i in range(len(temperatures)):
# #         j = i
# #         while j < len(temperatures):
# #             if temperatures[j] > temperatures[i]:
# #                 res.append(j - i)
# #                 break
# #             if j == len(temperatures) - 1:
# #                 res.append(0)
            
# #             j += 1

# #     return res

# def dailyTemperatures(temperatures):

#     res = ["0"] * len(temperatures)
#     while :
#         stack = temperatures
#         current = stack.pop()
#         difference = 0
#         while len(stack) > 0:
#             if stack.pop() <= current:
#                 difference += 1
#             else:
#                 i = difference
#                 break 
#     return res


def dailyTemperatures(temperatures):
    # loop through each element
    # repeat: if that element is greater than the top element in the stack, pop it and add the difference between
    # the current element and the popped one 
    # add that element to the stack 

    res = [0] * len(temperatures)
    stack = []
    for i, temp in enumerate(temperatures):
        while len(stack) != 0 and temp > stack[-1][1]:
            res[stack[-1][0]] = i - stack[-1][0]
            stack.pop()
        stack.append((i, temp))

    return res 

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))