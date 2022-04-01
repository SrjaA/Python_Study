import random

alian_number=random.randint(1,10)
alian_color=random.randint(1,2)
print(alian_number,alian_color)
first_number=int(input('Введите первое число: '))
second_number=int(input('Введите второе число: '))
while first_number!=5 and second_number!=5:
    if first_number==alian_number and second_number==alian_color:
        print('win')
    break
else:
    print('You loose')
    # first_number=int(input('Введите первое число: '))
    # second_number = int(input('Введите второе число: '))

print("Программа подбросит монетку 100 раз и покажет, сколько раз выпадет Орел или Решка\n")
tries = 0
damage = 1
orel = 0
reshka = 0
while tries !=100:
    tries += damage
    result = random.randint (1, 2)
    print("Осталось бросков: ", (100-tries))
    if result == 1:
        reshka += 1
    else:
        orel += 1
print("Орлов выпало: ", orel, "Решек выпало: ", reshka)
input("\nНажмите Enter, чтобы выйти.")

if alian_color==1:
    alian_color='Red'
else:
    alian_color='Black'

if first_number!=alian_number or second_number!=alian_color:
    print(alian_number,alian_color)
#
#
# text=[(i<0) for i in range(first_number,second_number)]
# print(text)
#
# for i in text:
#     if i<0:
#         print(i)
#     i+=1