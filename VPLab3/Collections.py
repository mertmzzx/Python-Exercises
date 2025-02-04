'''
s = list()
s1 = list('Python')
print(s)
print(s1)

s.append(5)
s.append(10)
s.append(20)
print(s)
'''
import random

'''
A = list (k for k in range(1,21) if 9<k<=30)
print(A)
'''

'''
s = [1, 2, 3, 4, 5, 6]

print(s[::-1]) #извеждаме елементите в обратен ред
print(s[:-1])  #принтираме без последния елемент
print(s[1:])   #принтираме без първия елемент
print(s[0:2])  #принтираме първите два елемента
print(s[-1:])  #принтираме последния елемент
'''

''' събиране на списъци
s = [4, 2]
s1 = [9, 10]
print(s + s1)
'''

'''
s = [[1,2,3,4], ['a', 'b', 'c'], [10,20]]
print(s[0][3]) #достъпваме 4тия елемент на първия списък
print(s[2][0]) #достъпваме 1вия елемент на третия списък
'''

''' 1-ви вариант на обхождане
s = [1, 2, 3, 4, 5, 6]
for i in s:
    print(i, end=' ')
'''

''' 2-ри вариант на обхождане
s = [1, 2, 3, 4, 5, 6]
for i in range(len(s)) : print(s[i], end = ' ')
'''

'''
s = [2, 4, 6, 8, 2]
print(4 in s)
print(s.index(4))
print(s.count(2))
print(max(s))
print(min(s))
'''

'''
s = [2, 4, 6, 8, 2]
s.append(22)
print(s)

s += [44, 88]
print(s)

s.insert(0, 90)
print(s)

s.remove(2)
print(s)

s.pop(0)
print(s)

del s[4]
print(s)
'''

'''
s = [2, 4, 6, 8, 2]
random.shuffle(s)
print(s)

print(random.choice(s))

s.reverse()
print(s)
'''

'''
s = [45, 10, 55, 5, 35]
s.sort()
print(s)

s.sort(reverse=True)
print(s)
s1 = ['s', 'T', 'a', 'E', 'f']
s1.sort(key=str.lower)
s1.sort()
print(s1)
'''

''' Кортеж
tup = tuple([10, 20, 30]) # преобразуване на списък в кортеж
print(tup)
tup1 = tuple('python') # преобразуване на низ в кортеж
print(tup1)
tup2 = tuple()
'''

'''
k = (7, 5, 3, 6, 1)
print(k[0]) #достъп до пелемент по индекс
print(k[2:3])
print(7 in k)
print(k * 3) #повторение
tup = k + (2,4) #конкатенация
print(tup)
'''

'''
tup = (7, 5, 3, 6, 1)
print(tup.index(1))
print(tup.count(5))
'''

'''Речник
d = dict()
d1 = dict(name='ivan', last_name='petrov')
d2 = dict([('name', 'polina'), ('l_name', 'koleva')])
print(d1)
print(d2)
'''

'''
d = { }
d['name'] = 'petyr'
d['l_name'] = 'kolev'
print(d)

d1 = {'name':'ivan', 'last_name':'ivanov'}
print(d1)

d3 = d.copy()
print(d3)
'''
'''
d = {'name':'ivan', 'last_name':'ivanov'}
print(d['name'])

b = 'fname' in d #проверяваме дали даден ключ съществува в речника
print(b)

print(len(d)) #получаваме броя на ключовете в речника

d['s_name'] = 'petrov'
print(d)

del d['s_name']
print(d)
'''
'''
for key in d.keys():
    print("( {0} => {1} )".format(key, d[key]), end=' ')
'''
'''
keys = list(d.keys())
keys.sort()
for key in keys:
    print("( {0} => {1} )".format(key, d[key]), end=' ')
'''