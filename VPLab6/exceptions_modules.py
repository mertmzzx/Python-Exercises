
'''

try:
    print('Hello')
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')

try:
    print('x')
except:
    print('Something went wrong')
finally:
    print('The try except is finished')
'''

'''
while True:
    try:
        x = int(input('Please enter a number: '))
        break
    except ValueError:
        print('Oops! That was no valid number. Try again...')
'''
'''
x = "a"
if not type(x) is int:
    raise TypeError('Only integers are allowed')
if x < 0:
    raise Exception('Sorry, no numbers below zero')
'''

'''
import mymodule
mymodule.greeting('Jonathan')

import dic
a = dic.person1['age']
print(a)
'''

'''
import math
content = dir(math)
print(content)
'''

import Phone

Phone.pots()
Phone.lsdn()
Phone.g3()