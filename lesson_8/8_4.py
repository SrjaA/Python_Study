import random

a=(1,2,3,4,5,6)
print(type(a))

b=[1,2,3,4,5,6]

print(a.__sizeof__())
print(b.__sizeof__())

b=(1)
print(type(b))
b=(1,)
print(type(b))

nested=(1,'do',['param',10,20])
nested[2][1]=15
print(nested)

c=(1,2,3,4,5,6)
d=(1,2,3,4,5,6)
if c!=d:
    print('danunanu')
else:print('ugoo')
import random
a=(1,2,3,4,5,5)
print('max',max(a),'min', min(a))
a=[random.randint(1,20) for i in range(10)]

print(a)
b=tuple(a)
print('max',max(b),'min', min(b))
c='gfkjelkjldfkjz9453'
print('max',max(c),'min', min(c))

a=tuple([random.randint(0,5) for i in range(10)])
b=tuple([random.randint(-5,0) for i in range(10)])
c=a+b
d=c.count(0)
print(c)
print(d)
print(sum(a))
ea=('1','2','3','4','5','5','eflkl')
#print(sum(ea))
print(ea, type(ea))
z=','.join(ea)
print(z,type(z))

if sum(a)>sum(b):
    print(sum(a))
else: print(sum(b))
print(a.index(min(a)),b.index(min(b)))
