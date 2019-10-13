def solution(arrangement):
    answer = 0
    stack = list()
    previous = ''
    for arr in arrangement:
        if not stack:
            stack.append(arr)
        else:
            if stack[-1] == '(' and arr == ')':
                pop = stack.pop()
                if previous == ')':
                    answer += 1
                else:
                    answer += len(stack)
            elif arr == '(':
                stack.append(arr)
        previous = arr
    return answer