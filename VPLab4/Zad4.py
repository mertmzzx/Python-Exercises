string = input()

count = len(string.split(" "))

for i in string.split(" "):
    print(i * count, end= "")