def solution(L, x, l, u):
    if l==u and L[(l+u)//2] != x:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid -1)
    else:
        return solution(L, x, mid+1, u)

# 정확성:100, 효울성:100