try:
    k=1/0
except ZeroDivisionError:
    k=0
print(k)

my_dict={'a':1,'b':2,'c':3}

try:
    value=my_dict['d']
except (IndexError,KeyError):
    print('произошла ошибка')

try:
    value=my_dict['d']
except KeyError:
    print('произошла ошибка')
finally:
    print('"finally" possible')

try:
    value=my_dict['d']
except KeyError:
    print('произошла ошибка')
else:
    print('ошибок не прозошло')