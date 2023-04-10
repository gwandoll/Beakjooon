from collections import deque
f,s,g,u,d = map(int,input().split())
visited = [0] *(f+1)

def bfs(n):
    queue = deque()
    queue.append(n)
    visited[n] = 1
    while queue:
        x = queue.popleft()
        if x == g:
            return visited[g]-1
        for i in (x+u,x-d):
            if 0 < i and i <= f and not visited[i]:
                visited[i] = visited[x]+1
                queue.append(i)


    return "use the stairs"
    
print(bfs(s))