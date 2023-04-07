from sys import stdin
import heapq

h = []
n = int(stdin.readline())

for i in range(n):
    a = int(stdin.readline())
    if a == 0 :
        if len(h) ==0:
            print(0)
        else:
            b = -heapq.heappop(h)
            print(b)
    else:
        heapq.heappush(h,-a)