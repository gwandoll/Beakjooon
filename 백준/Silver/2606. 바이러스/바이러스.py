n = int(input())
m = int(input())

visited = [0]*(n+1)
graph = [[False]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True
    
    
def dfs(v,graph,visited):
    visited[v] = True
    for i in range(1,len(graph[v])):
        if graph[v][i] == True and visited[i] == 0:
            dfs(i,graph,visited)
            
dfs(1,graph,visited)
print(visited.count(True)-1)