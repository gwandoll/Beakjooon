n = int(input())
for _ in range(n):
    a,b = map(str, input().split())
    print(b[:int(a)-1] + b[int(a):])