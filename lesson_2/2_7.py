a = int(input('Введите превое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a > b and a > c:
    print('a больше b и c')
elif b > a and b > c:
    print('b больше a и c')
else:
    print('с больше a и b')
