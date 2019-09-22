from collections import deque


def solution(progresses, speeds):
    answer = list()
    queue = deque()
    a = 1
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] != 0:
            queue.append(((100 - progresses[i]) // speeds[i]) + 1)
        else:
            queue.append((100 - progresses[i]) // speeds[i])

    pop = queue.popleft()
    while queue:
        if pop >= queue[0]:
            queue.popleft()
            a += 1
        else:
            answer.append(a)
            a = 1
            pop = queue.popleft()
    answer.append(a)

    return answer