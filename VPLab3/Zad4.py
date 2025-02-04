n = int(input())
list = list()
d = dict()
for i in range(1, n+1):
    list.append(i)
    d[i] = n
    n = int(n-1)
print(d)