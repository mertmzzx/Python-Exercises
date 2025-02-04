# MNOJESTVA
'''
s = set([1, 2, 3, 1])
print(s)

s2 = set("hello")
for i in s2:
    print(i, end=' ')

print(len(s2))
'''

'''
a = set([1,2,3])
b = set([4, 2, 6])

s1 = a | b
print(s1)

s2 = a & b
print(s2)

s3 = a - b
print(s3)
'''

'''
s1 = set([2,4,6, 8, 10])
s1.add(12)
s1.remove(12)
s1.pop()
s1.discard(5)
print(s1)
'''

#STRINGS
s = "123"
print(s[0])

s1 = "Hello"
print(s1[:]) 
print(s1[:-1:])
print(s1[1::2])
print(s1[1::])