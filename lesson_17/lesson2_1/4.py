import math
import pyttsx3
from math import sqrt

#1
mas_1=[i for i in input().split()]

for i in mas_1:
    if mas_1.count(i)<2:
        print(i)
exit()
# 2
x = [y for y in input().split()]
print(x)
m = set(x)
print(m)
print(len(x) - len(m))

# 3

t_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
t_2 = (45, 21, 124, 76, 5, 23, 91, 234)

if sum(t_1) > sum(t_2):
    print(f'Сумма больше в кортеже {t_1}')
    print(f'Индекс максимального элемента: {t_1.index(max(t_1))}')
else:
    print(f'Сумма больше в кортеже {t_2}')
    print(f'Индекс максимального элемента: {t_2.index(max(t_2))}')

# 4
str = 'An apple a day keeps the doctor away'
sds = {i: str.count(i) for i in str}
print(sds)

# 5

engine=pyttsx3.init()
engine.setProperty('rate', 150)     # скорость речи
engine.setProperty('volume', 0.9)   # громкость (0-1)



cake = {'наполон': [['масло', 'мука', 'сахар'], 6.5, 2010],
          'медовик': [['мука', 'сахар', 'honey'], 7.8, 1570],
          'киевский': [['galushki', 'мука', 'соль'], 15, 340]}

choice = "If you want to see a description, enter 1." \
         "View price - enter 2." \
         "View quantity - enter 3. " \
         "View all information - enter 4." \
         "If you want to buy a cake, enter 5." \
         "To exit the program, enter 0"

engine.say(choice)      # запись фразы в очередь
engine.say("Я могу говорить!")  # запись фразы в очередь

buy = input('Какое торт Вас интересует: ')
look = input('Что Вы хотели бы уточнить: ')

for k, v in cake.items():
    if buy == k:
        if look == 'описание':
            print(f'Торт {buy} состоит из ', *v[0])
        elif look == 'цена':
            print(f'Торт {buy} стоит {v[1]} рублей')
        elif look == 'количество':
            print(f'Торта {buy} в наличии {v[2]} грамм')

amount = int(input('Скока вешать?: '))

for k, v in cake.items():
    if buy == k:
        bought = amount * v[1] / 100
        print(f'к оплате {bought}')
        print(f'Торта {buy} осталось {v[2] - amount} грамм')
print('Дзякуй, заходзьце')

# 6

q_1 = [int(i) for i in input().split()]
q_2 = [int(i) for i in input().split()]
w = 0

for i in q_1:
    if i in q_2:
        w += 1
print(f'Одинаковых чисел: {w}')

# 7

try:
    a = int(input('first number: '))
    b = int(input('second number: '))
    c = a * sqrt(a) / b * math.pi
except (ZeroDivisionError, ValueError, Exception):
    print('произошла ошибка')
else:
    print('result', c)
finally:
    print('konec')

#8

sum = 0
n = 0
with open('file_1.txt', 'r') as f:

    for i in f:
        g = int(i[-2])
        sum += g
        n += 1
        if g < 3:
            print(i[:-1])
    print('Средни балл: % .2f’ % (suma / n)')


print(f'Всего {n} оценок')

