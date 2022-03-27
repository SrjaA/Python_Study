import random

a=[2,6,7,4,0,15,8,45,65,2,34]
c=[b for b in range(random.randint(1,20))]
print(c)
k=0
l=0
try:
    for i in c:
        if i//3==0:
            k+=1
        elif i%2==0:
            l+=i
        else: continue
except (ZeroDivisionError):
    print('бяда')
n=l/(len(c)-k)
print('чисел/3 - ', k,':::' 'среднее арифметическое - ',n)