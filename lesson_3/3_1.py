x=int(input('Введите первое число: '))
y=input('Введите знак + - * /: ')
z=int(input('Введите второе число: '))

if y=="+":
    print(x+z)
elif y=="-":
    print(x-z)
elif y=="*":
    print(x*z)
else:
    print(x/z)