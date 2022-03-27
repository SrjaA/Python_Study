class Human:

    # Статические поля
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        # Динамические поля
        # Публичные
        self.name = name
        self.age = age
        # Приватные
        self.__money = 0
        self.__house = None
    def info(self):
        print('Name:', self.name)
        print('Age:', self.age)
        print('Money:', self.__money)
        print('House:',self.__house)

    # Статический метод
    @staticmethod
    def default_info():
        print('Default Name: ', Human.default_name)
        print('Default Age: ', Human.default_age)

    def earn_money(self, amount):
        self.__money += amount
        print(f'Earned {amount} money! Current value: ', self.__money)

Human.default_info()
alexander = Human('Sasha', 27)
alexander.info()
alexander.earn_money(5000)
alexander.earn_money(20000)
alexander.info()

