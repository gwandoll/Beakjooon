from collections import deque
m,n = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
lst = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            lst.append([i, j])


dx = [1,-1,0,0]
dy = [0,0,-1,1]



def bfs(queue):
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >=m:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
res = 0
bfs(lst)               
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)