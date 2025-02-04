n = int(input())
for i in range(1, 1 + n):
    for j in range(i, n * n + 1, n):
        print(j, end=" ")
    print()