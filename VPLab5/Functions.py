'''
def f():
    s = '-- Inside f()'
    print(s)

print('Before calling f()')
f()
print('After calling f()')

def f1(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')

f(6, 'bananas', 1.74)


def f2():
    print('foo')
    print('bar')
    return

f2()
'''
'''
def f(x):
    if x < 0:
        return
    if x > 100:
        return
    print(x)

f(-3)
f(105)
f(64)
'''
'''
def f():
    return 'foo'

s = f()
print(s)
'''
'''
def psum(*k):
    result = 0
    for i in k:
        result += i
    return result

s = psum(1,2,3,4)
print(s)
'''


#Lambda
'''
num = 10
L = lambda n:2*n+1

print('нечетни числа:')
for k in range(num):
    print(L(k), end=' ')

#директно извикване на ламбда
print('\nквадрати на числата:')
for k in range(num):
    print((lambda x:x*x) (k+1), end=' ')
'''

def func():
    global varl
    varl = 10
varl= 5
print(varl)

func()
print(varl)