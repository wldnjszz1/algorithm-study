from collections import deque


def solution(priorities, location):
    compare = [p for p in priorities]
    highest = max(compare)
    priorities = [(priority, i) for i, priority in enumerate(priorities)]
    queue = deque(priorities)
    answer = list()

    while queue:
        pop = queue.popleft()
        if pop[0] < highest:
            queue.append(pop)
        else:
            answer.append(pop)
            compare.remove(highest)
            if not compare:
                break
            highest = max(compare)

    for i, a in enumerate(answer):
        if location == a[1]:
            return i + 1