a = int(input())

for i in range(a):
    b = input()    
    sc = 0
    sco = 0
    for i in b:
        if i == "O":
            sc +=1
            sco += sc
        else:
            sc = 0
    print(sco)    