import sys

maxEven = 0
minOdd = sys.maxsize

sumEven = 0
countEven = 0
sumOdd = 0
countOdd = 0

for i in range(10):
    num = int(input())
    if  num % 2 == 0:
        if num > maxEven:
            maxEven = num
        sumEven += num
        countEven += 1
    else:
        if num < minOdd:
            minOdd = num
        sumOdd += num
        countOdd += 1

print(f'Максималното четно число е {maxEven}')
print(f'Минималното нечетно число е {minOdd}')
print(f'Сумата на нечетните числа е {sumOdd}')
print(f'Сумата на четните числа е {sumEven}')
print(f'Броят на четните числа в поредицата е {countEven}')
print(f'Броят на четните числа в поредицата е {countOdd}')