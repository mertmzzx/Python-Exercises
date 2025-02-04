list = list()

for i in range(1, 101):
    if i % 2 == 0 and i % 5 == 0:
        list.append(i)

list.reverse()
print(list)