test = []
n = int(input())
book = dict()
for i in range(n):
    bn = input()
    if book.get(bn):
        book[bn]= book[bn]+1
    else:
        book[bn]=1

for i in book.keys():
    if max(book.values())==book[i]:
        test.append(i)
test.sort()
print(test[0])