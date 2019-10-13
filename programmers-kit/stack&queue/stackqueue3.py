def solution(heights):
    answer = [0] * len(heights)
    for i in range(len(heights)-1, 1, -1):
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                answer[i] = j + 1
                break
    return answer


if __name__ == "__main__":
    print(solution([6,9,5,7,4]))

