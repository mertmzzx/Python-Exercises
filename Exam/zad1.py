from audioop import reverse

l1 = list()
for i in range(10):
    n = int(input())
    if n > 0:
        l1.append(n)
    else:
        print("Невалидно число")

l1.sort(reverse=True)
print(l1)

l2=list()
for i in l1:
    if i % 2 == 0:
        l2.append(i)
l2.sort(reverse=True)
print(l2)