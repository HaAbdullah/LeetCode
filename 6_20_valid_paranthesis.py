def isValid(s):
    myStack = []
    for i in s:
        if i == '(' or i == '[' or i == '{':
            myStack.append(i)
        elif len(myStack) > 0:
            if i == ')' and myStack[-1] == '(':
                myStack.pop()
            elif i == ']' and myStack[-1] == '[':
                myStack.pop()
            elif i == '}' and myStack[-1] == '{':
                myStack.pop()
            else:
                return False
        else: return False
    return True if len(myStack) == 0 else False


print(isValid("(])"))
# print(isValid("([])"))

myarray = ["hi", "hello"]
print(myarray.pop())
print(myarray.pop())
