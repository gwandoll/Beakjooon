from collections import deque

graph = []
lst = []
n,m = map(int,input().split())
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(n,m):
    queue = deque()
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        #네가지 방면 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #공간 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #0인곳 무시
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if graph[nx][ny] ==1 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(n,m))