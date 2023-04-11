import sys
sys.setrecursionlimit(100000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y, k):
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny <0 or ny >=n:
            continue
        if graph[nx][ny] <= k:
            continue
        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx,ny,k)


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = 1
for k in range(max(map(max, graph))):
    visited = [[False]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                count += 1
                visited[i][j] = True
                dfs(i, j, k)
    ans = max(ans, count)

print(ans)