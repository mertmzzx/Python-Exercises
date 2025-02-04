num = input()

list = list()
for i in num:
    list.append(int(i))

tup = tuple(list)
list.reverse()
tup1 = tuple(list)

print(tup)
print(tup1)