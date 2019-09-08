def solution(s):
    answer = 0
    for ss in s:
        if ss.lower() == 'p':
            answer += 1
        elif ss.lower() == 'y':
            answer -= 1
    return answer == 0