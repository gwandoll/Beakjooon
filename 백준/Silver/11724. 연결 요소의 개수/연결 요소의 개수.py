from collections import deque

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(graph,visited,start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            
count = 0            
for i in range(1, n + 1):
    if not visited[i]:  
        if not graph[i]:  
            count += 1  
            visited[i] = True 
        else:  
            dfs(graph,visited,i)  
            count += 1  
            
print(count)