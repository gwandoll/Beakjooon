n,m,v = map(int,input().split())

lst = []
graph = [[0] * (n+1) for i in range(n+1)]
visited = [0] * (n+1)
visited1 = [0] * (n+1)

for i in range(m):
    d,f = map(int,input().split())
    graph[d][f] = 1
    graph[f][d] = 1
    
def dfs(v,graph,visited):
    visited[v] = 1
    print(v,end = ' ')
    for i in range(1,len(graph[v])):
        if  graph[v][i] == 1 and visited[i] == 0:
            dfs(i,graph,visited)
            
from collections import deque
def bfs(v,graph,visited1):
    queue = deque([v])
    visited1[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(1,len(graph[v])):
            if graph[v][i] == 1 and visited1[i] == 0:
                queue.append(i)
                visited1[i] = 1
    
dfs(v,graph,visited)
print()
bfs(v,graph,visited1)