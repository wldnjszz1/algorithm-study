def solution(v):
    direct, answer = 0, 0
    answer_list = list()
    v.sort()
    small_v = v[:len(v)//2]
    big_v = v[len(v)//2:]

    for i, (s, b) in enumerate(zip(small_v, big_v)):
        if direct == 0:
            answer_list.insert(i, b)
            answer_list.append(s)
            direct = 1

        else:
            answer_list.insert(i, s)
            answer_list.append(b)
            direct = 0

    for i in range(len(answer_list) - 1):
        answer += abs(answer_list[i] - answer_list[i + 1])

    return answer


if __name__ == "__main__":
    print(solution([20, 8, 10, 1, 4, 15]))
