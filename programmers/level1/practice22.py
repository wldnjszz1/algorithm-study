def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)
    a = ''.join(answer)
    return int(a)