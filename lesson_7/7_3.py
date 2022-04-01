import random
a=random.randint(1,1000)
b=random.randint(1,1000)
print(a,b)
if a%2==0 and b%2==1:
    print(b)
elif a%2==1 and b%2==0:
    print(a)
elif a%2==0 and b%2==0:
    print('twice chotnie')
else: print('twice nechotnie')