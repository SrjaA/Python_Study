import random

h = int(input())
g = int(input())
list1 = []
i = 1
t=0
while i <= h:
    a = random.randint(0, 9)
    list1.append(a)
    i += 1
print(list1)

for m in list1:
    if g in list1[m]:
        t+=1
print(t)

import random
a=int(input(''))
b=[random.randint(1,20) for i in range(a)]
c=int(input())
d=0
for i in b:
    for j in str(i):
        j=int(j)
        if j==c:
            d+=1
    print(d)