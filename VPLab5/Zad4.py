l1 = [14, 5, -15, 10, 20, 45, 1]
n = int(input())

def f(list, n):
    for i in range(len(list)):
        if  list[i] >= n:
            list[i] = 0
    print(list)

f(l1, n)