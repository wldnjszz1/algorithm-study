def solution(s):
    answer = []
    small = ''
    big = ''
    for ss in s:
        answer.append(ss)
    answer.sort(reverse=True)
    for a in answer:
        if a != a.lower():
            big += a
        else:
            small += a
    print(small, big)
    return small+big