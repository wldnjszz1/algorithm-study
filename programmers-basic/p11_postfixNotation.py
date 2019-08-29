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


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(S):
    opStack = ArrayStack()
    answer = ''
    for i in S:
        if i == ')':
            for a in range(opStack.size()):
                p = opStack.pop()
                if p == '(':
                    break
                else:
                    answer += p
        elif i in '*/+-(':
            if opStack.isEmpty():
                opStack.push(i)
            else:
                if i == '(':
                    opStack.push(i)
                elif prec[opStack.peek()] < prec[i]:
                    opStack.push(i)
                else:
                    p = opStack.pop()
                    answer += p
                    opStack.push(i)
        else:
            answer += i
    while not opStack.isEmpty():
        p = opStack.pop()
        answer += p
    return answer


if __name__ == "__main__":
    print(solution('A*(B+C)'))
