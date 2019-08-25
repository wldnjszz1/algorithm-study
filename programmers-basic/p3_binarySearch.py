from builtins import len


def solution(L, x):
    lower = 0
    upper = len(L)-1
    while lower <= upper:
        middle = (lower + upper)//2
        if lower == upper:
            return -1
        if L[middle] == x:
            return middle
        elif L[middle] < x:
            lower = middle +1
        elif L[middle] > x:
            upper = middle -1
    else:
        return -1

# 정확성 100, 효울성 85