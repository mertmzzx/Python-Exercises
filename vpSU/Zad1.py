# 1,4,6,8,10

n1 = input()
n2 = input()
digits = set()

for i in n1:
    for j in n2:
        if i == j:
            digits.add(i)

for i in digits:
    print(i, end= " ")