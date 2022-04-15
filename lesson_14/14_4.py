
def summ(n, m):
    return n + m


def subs(n, m):
    return n - m


def mult(n, m):
    return n * m


def divis(n, m):
    try:
        return n / m
    except ZeroDivisionError:
        return 'Error! Division by zero!'


while True:
    sign = input('Enter sign: ')
    if sign == '0':
        exit()
    if sign not in ('+', '-', '*', '/', '0'):
        print('Default sign')
        continue
    x, z = float(input('Enter first number: ')), float(input('Enter second number: '))
    if sign == '+':
        print(summ(x, z))
    elif sign == '-':
        print(subs(x, z))
    elif sign == '*':
        print(mult(x, z))
    elif sign == '/':
        print(divis(x, z))
