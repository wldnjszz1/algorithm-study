def solution(n):
    answer = list()
    for i in range(1, n + 1):
        if n % i == 0:
            answer.append(i)

    return sum(answer)