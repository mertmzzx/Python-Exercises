import random

list = list()
for i in range(0,6):
    n = random.randint(1, 20)
    list.append(n)

print(list)

for i in range(0, len(list), 3):
    num = list[i+1] + list[i + 2]
    list.insert(i+2, num)
print(list)