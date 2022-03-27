import random

t = 0
i = 1
list1 = []
while i < 8:
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    x = int(input())
    y = int(input())
    if x > a and y > b:
        t += 1
    print('давай по новой, Миша')
    if i == 4:
        list1.append(a)
        list1.append(b)
    i += 1
if t >= 4:
    print(f'''Your pairs оказались больше {t} раз(a)
    А в четвертой итерации {list1}''')
print(list1)
