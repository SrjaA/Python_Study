import random
# Используем random для выбора своего варианта КНБ
al_input = random.randint(1, 3)
# Обращаемся к пользователю с необходимостью ввести вариант
print('Привет! Давай перенесёмся в детство :)')
print('И сыграем в КНБ')
print('Выбирай и вводи в поле ниже свой вариант, где')
print('1 - Камень, 2 - Ножницы, 3 - Бумага')

# Считываем введённое значение и печатаем подтверждение
us_input = int(input('Enter: '))
if us_input == 1:
    print('Your select - ROCK!')
elif us_input == 2:
    print('Your select - SCISSORS!')
elif us_input == 3:
    print('Your select - PAPER!')
else:
    print('Enter only 1, 2 или 3 :)')

# Производим сравнение и печатаем исход игры
if al_input == us_input:
    print('Ничья!')
elif (al_input == 1 and us_input == 3) or (al_input == 2 and us_input == 1) or (al_input == 3 and us_input == 2):
    print('You WIN!')
elif (al_input == 1 and us_input == 2) or (al_input == 3 and us_input == 1) or (al_input==2 and us_input==3):
    print('You lose')
else:
    print('Game Over')

# Показываем свой выбор
if al_input == 1:
    print('У меня Камень')
elif al_input == 2:
    print('У меня Ножницы')
else:
    print('У меня Бумага')
