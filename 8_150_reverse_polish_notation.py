def evalRPN(tokens):
    myStack = []
    for token in tokens:
        if token == '+':
            a = int(myStack.pop())
            b = int(myStack.pop())
            c = a + b 
            myStack.append(c)
        elif token == '-':
            a = int(myStack.pop())
            b = int(myStack.pop())
            c = b - a 
            myStack.append(c)
        elif token == '*':
            a = int(myStack.pop())
            b = int(myStack.pop())
            c = a * b 
            myStack.append(c)
        elif token == '/':
            a = int(myStack.pop())
            b = int(myStack.pop())
            c = b / a 
            myStack.append(c)
        else:
            myStack.append(token)

        print(myStack)
    return int(myStack[0])


#print(evalRPN(["2","1","+","3","*"]))
#print(evalRPN(["4","13","5","/","+"]))
#print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))