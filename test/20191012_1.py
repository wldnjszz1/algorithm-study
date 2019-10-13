def solution(N):
    answer = list()
    str_n = ""
    check = N
    product = 1
    answer_list = list()

    for i in range(2, N):
        while check > 0:
            str_n += str(check % i)
            check = check // i

        answer.append(str_n[::-1])
        str_n = ""
        check = N
    answer.append(str(N))

    for i, a in enumerate(answer):
        for string in a:
            if string != '0':
                product *= int(string)
        answer_list.append([i + 2, product])
        product = 1

    answer_list.sort(key= lambda x: (x[1], x[0]), reverse=True)
    return answer_list[0]


if __name__ == "__main__":
    print(solution(14))
