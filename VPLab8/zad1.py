from logging import exception

n = int(input())
l1 = list()
count1 = 0
minIndex = 0
try:
    if n < 35 and n > 15:
        for i in range(n):
            num = int(input())

            if num < 300 and num > 30:
                l1.append(num)
            else:
                raise Exception()
        for i in l1:
            des = 0
            if i > 100:
                des = (i // 10) % 10
            else:
                des = i // 10
            if des % 3 == 0:
                count1 += 1
    else:
        raise Exception()
    for i in range(n):
        minNum = 0
        if l1[i] > minNum and l1[i] % 6 == 4:
            minNum = l1[i]
            minIndex = i
except:
    print("Invalid values")

l2 = list()

for i in l1:
    if i > 10 and i % 2 == 0 and i % 3 == 0 and i < 100:
        l2.append(i)

sum = 0
count2 = 0
for i in range(len(l2)):
    if i % 3 == 0:
        sum += l2[i]
        count2 += 1
avg = sum / count2

minNum = 0
for i in l2:
    if i % 2 == 0 and i > minNum:
        minNum = i
l2.remove(minNum)

maxN = 30
minN = 300
for i in l2:
    if i % 3 == 0:
        if i < minN:
            minN = i
        elif i > maxN:
            maxN = i
el = minN * maxN
l2.insert(0, el)







