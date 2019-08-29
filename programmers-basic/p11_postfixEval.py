class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            for i in range(opStack.size()):
                p = opStack.pop()
                if p != '(':
                    postfixList.append(p)
                else:
                    break
        else:
            if opStack.isEmpty():
                opStack.push(token)
            elif prec[opStack.peek()] < prec[token]:
                opStack.push(token)
            else:
                p = opStack.pop()
                postfixList.append(p)
                opStack.push(token)

    while not opStack.isEmpty():
        p = opStack.pop()
        postfixList.append(p)

    return postfixList


def postfixEval(tokenList):
    valStack = ArrayStack()
    for token in tokenList:
        if type(token) is int:
            valStack.push(token)
        elif token == '*':
            second = valStack.pop()
            first = valStack.pop()
            valStack.push(first*second)
        elif token == '/':
            second = valStack.pop()
            first = valStack.pop()
            valStack.push(first/second)
        elif token == '+':
            second = valStack.pop()
            first = valStack.pop()
            valStack.push(first+second)
        elif token == '-':
            second = valStack.pop()
            first = valStack.pop()
            valStack.push(first-second)
    return valStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val


if __name__ == "__main__":
    print(splitTokens('7 * (9 - (3+2))'))
    print(infixToPostfix(splitTokens('7 * (9 - (3+2))')))
    print(postfixEval(infixToPostfix(splitTokens('7 * (9 - (3+2))'))))
