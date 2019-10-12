def solution(a, b, c):
    if b == 0:
        return 1;
    else:
        if b % 2 == 0:
            result = solution(a, b // 2, c)
            return result*result % c
        else:
            result = solution(a, b - 1, c)
            return result*a % c

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(solution(a, b, c))


#
# a, b, c = map(int, input().split())
# print(pow(a, b, c))