n = int(input())
lst = []
cnt = 0
c = -1
for i in range(n):
    a,b = map(int,input().split())
    lst.append([a,b])
    
lst.sort(key=lambda x: (x[1],x[0]))

for i,j in lst:
    if i >= c:
        cnt += 1
        c = j
        
print(cnt)