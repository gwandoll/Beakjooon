from sys import stdin
stack = []
n = int(stdin.readline())
for _ in range(n):
    a = stdin.readline().split()
    if a[0] == "push":
        stack.append(int(a[1]))
    elif a[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            b = stack.pop()
            print(b)
    elif a[0] == "size":
        print(len(stack))
    
    elif a[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])