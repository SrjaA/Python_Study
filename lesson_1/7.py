import random
#Генерируем случайное 3-значное число
x=random.randint(100, 999)
print('Номер Вашего бочонка - ',x)
#Определяем целое число сотых
y=(x-x%100)/100
#Вычисляем разницу между случайным числом и его целых сотых
d=x-(y*100)
#Определяем число единиц
z=d%10
#Определяем число десятков
s=(d-z)/10
# сумма
sum123=int(y+z+s)

print('А сумма всех его цифр - ', sum123,'! Представляете?')