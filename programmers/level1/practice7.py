def solution(arr):
    answer = list()
    x = 0
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        if i == answer[x]:
            continue
        else:
            answer.append(i)
            x += 1
    return answer