'''
for letter in range(ord('a'), ord('z')+1):
    print(chr(letter))

word = 'Python'
for letter in word:
    print(letter)

n = int(input('enter number: '))
sum = 0
while True:
    sum += n % 10
    n = n // 10
    if not n:
        break
print(sum)


for number in range(1, 20):
    if number == 5:
        continue
    if number == 11:
        break
    print(number)


for n in range(20, 10, -2):
    print(n)
'''

''' #1
n = int(input())
biggestNum = 0
for i in range(n):
    number = int(input())
    if number > biggestNum:
        biggestNum = number
print(biggestNum)
'''

''' #2
n = int(input())
sum = 0
for i in range(n):
    number = int(input())
    sum += number
print(sum)
'''

''' #3
n = int(input())

for i in range(n+1):
    for j in range(i):
        print('*', end = ' ')
    print()
'''

''' #4
number = int(input())
prime = True
if number == 0 or number == 1:
    prime = False

for i in range(2, number):
    if number % i == 0:
        prime = False
        break;

if prime:
    print('Числото е просто')
else:
    print('Числото не е просто')
'''

'''
Програма която проверява дали едно число въведено от потребителя се 
намира в интервала от 5 до 25(включително)
и да извежда стойността и дали лежи в този интервал
'''
n = int(input())

if  n >= 5 and n <= 25:
    print(f'{n} се намира в интервала от 5 до 25.')
else:
    print(f'{n} не се намира в интервала от 5 до 25.')