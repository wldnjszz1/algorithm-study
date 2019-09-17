def solution(n, m):
    nn= n
    mm = m
    while n > 0:
        if m > n:
            n, m = m, n
        n = n % m
    return [m, (nn//m) * (mm//m) * m]