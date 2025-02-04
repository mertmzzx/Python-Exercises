word = input("Enter string: ")

t1 = tuple(word)

distance = int(input("Enter distance: "))

l1 = list()

for i in range(0, len(t1), distance):
    l1.append(t1[i])

t2 = tuple(l1)
print(t2)