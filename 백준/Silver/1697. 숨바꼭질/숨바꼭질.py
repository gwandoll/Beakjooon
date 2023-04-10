import sys
from collections import deque
n,k = map(int,input().split())

max = 100001
visited = [0] * max
def bfs(n,k):
    queue = deque()
    queue.append(n)
    
    while queue:
        x = queue.popleft()
        if x ==k:
            return visited[k]
        for i in (x-1,x+1,x*2):
            if 0 <= i and i < max and not visited[i]:
                visited[i] = visited[x] +1
                queue.append(i)

print(bfs(n,k))