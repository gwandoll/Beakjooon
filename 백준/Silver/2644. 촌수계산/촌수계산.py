from collections import deque
n = int(input())
a,b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] =1
    
    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if visited[i] == 0:
                visited[i] += visited[x] +1
                queue.append(i)

bfs(a)

if visited[b] != 0:
    print(visited[b]-1)
else:
    print(-1)