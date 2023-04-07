from collections import deque
from sys import stdin

queue = deque()

n= int(stdin.readline())
for i in range(n):
    a =  stdin.readline().split()
    if a[0] == 'push':
        queue.append(a[1])
    if a[0] == 'pop':
        if len(queue) > 0:
            a = queue.popleft()
            print(a)
        else:
            print(-1)
    if a[0] == 'size':
        print(len(queue))
    if a[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if a[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    if a[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])