# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
# (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.


def dfs(node):
    check[node] = True

    for a in adj[node]:
        if not check[a]:
            dfs(a)


N, M = map(int, input().split())

adj = [[] for _ in range(N + 1)]
check = [False] * (N + 1)
count = 0

for _ in range(M):
    v, e = map(int, input().split())
    adj[v].append(e)
    adj[e].append(v)

for i in range(1, len(adj)):
    if not check[i]:
        count += 1
        dfs(i)

print(count)

# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6