text = input()

l1 = list(text.split(" "))

longest = "a"
shortest = "Pneumonoultramicroscopicsilicovolcanoconiosis"

for i in l1:
    if len(i) > len(longest):
        longest = i
    if len(i) <= len(shortest):
        shortest = i

l1.remove(shortest)
l1.remove(longest)

for i in l1:
    print(i, end=" ")
