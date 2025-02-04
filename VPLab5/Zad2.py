num = int(input())

def f(num):
    n = str(num)
    n1 = n[::-1]
    if n == n1:
        print(1)
    else:
        print(0)

f(num)