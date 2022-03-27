import pyttsx3

engine=pyttsx3.init()
engine.setProperty('rate', 150)     # скорость речи
engine.setProperty('volume', 0.9)   # громкость (0-1)
ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
engine.setProperty('voice', ru_voice_id)
engine.say('Михалыч, погнали!')


cake = {'наполон': [['масло', 'мука', 'сахар'], 6.5, 2010],
          'медовик': [['мука', 'сахар', 'honey'], 7.8, 1570],
          'киевский': [['galushki', 'мука', 'соль'], 15, 340]}

choice = ["Выбирай давай торт уже!",
 "View price - enter 2.",
        "View quantity - enter 3. " ,
        "View all information - enter 4.",
         "If you want to buy a cake, enter 5.",
          "To exit the program, enter 0"]



engine.say(choice[0])
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


engine.runAndWait()