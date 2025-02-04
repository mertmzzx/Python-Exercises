import random

count = int(input())

l1 = list()

for i in range(count):
    num = random.randint(1, 20)
    l1.append(num)

print(l1)

lOdd = list()
lEven = list()

for i in range(count):
    if i % 2 == 0:
        lEven.append(l1[i])
    else:
        lOdd.append(l1[i])

lEven = sorted(lEven)
lOdd = sorted(lOdd, reverse=True)

print(lEven)
print(lOdd)
l1 = lEven + lOdd

print(l1)