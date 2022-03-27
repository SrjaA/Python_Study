class Human:

    default_name='No name'
    default_age=0
    def __init__(self,name=default_name,age=default_age):
        self.name=name
        self.age=age
        self.__money=0
        self.__house=None
    def info(self):
        print(self.name)
        print(self.age)
        print(self.__house)
        print(self.__money)

    @staticmethod
    def default_info():
        print(default_name)
        print(default_agge)

    def earn_money(self, qua):
        self.__money += qua
        print(f'Earned {qua} money! Current value: ', self.__money)

