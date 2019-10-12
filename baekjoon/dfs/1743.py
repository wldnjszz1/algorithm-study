N, M, K = map(int, input().split())
isle = [[0] * M for _ in range(N)]
visit = [[False] * M for _ in range(N)]
answer = 0
DELTAS = [(-1, 0), (0, 1), (0, -1), (1, 0)]

for _ in range(K):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    isle[r][c] = 1


def possible(a, b):
    return 0 <= a < N and 0 <= b < M


def dfs(x, y):
    global count
    for dx, dy in DELTAS:
        now_x, now_y = x + dx, y + dy
        if not possible(now_x, now_y) or not isle[now_x][now_y] or visit[now_x][now_y]:
            continue
        visit[now_x][now_y] = True
        count += 1
        dfs(now_x, now_y)
    return count


for i in range(N):
    for j in range(M):
        if isle[i][j] and not visit[i][j]:
            visit[i][j] = True
            count = 1
            answer = max(answer, dfs(i, j))

print(answer)

# 3 4 5
# 3 2
# 2 2
# 3 1
# 2 3
# 1 1