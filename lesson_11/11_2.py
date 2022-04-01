try:
    a=int(input('first number: '))
    b=int(input('second number: '))
    c=a/b
except ZeroDivisionError:
    print('произошла ошибка')
else:
    print('result*2', c**2, type(c**2))
finally:
    print('konec')