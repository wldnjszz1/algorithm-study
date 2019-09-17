def solution(n):
    nn = pow(n, 1/2)
    if nn == int(nn):
        return (nn+1)**2
    return -1