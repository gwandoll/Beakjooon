n = int(input())
graph= []
for i in range(n):
    graph.append(list(map(int,input())))
    
def dfs(x,y):
    global cnt
    #밖으로 벗어나면 종료
    if x <= -1 or x>= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 'True':
        graph[x][y] = cnt
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    
    return False


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
             graph[i][j] = 'True'

cnt = 1
num = []
num2 = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            cnt += 1
        num.append(graph[i][j])
        

for i in range(1,max(num)+1):
    num2.append(num.count(i))
num2.sort()

print(max(num))
for i in num2:
    print(i)