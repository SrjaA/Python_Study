try:
    a = int(input('first number: '))
    b = int(input('second number: '))
    c = a / b
except (ZeroDivisionError,ValueError,Exception):
    print('произошла ошибка')
else:
    print('result*4', c**4)

finally:
    print('konec')