def a_function():
    print('you just created a function!')


a_function()


def empty_function():
    pass


a = (2, 3, 4, 5, 3)


def mas_sum():
    print(sum(a))


mas_sum()


def add(a, b):
    return a + b


print(add(1, 2))


def keyword_function(a=1, b=2):
    return a + b


print(keyword_function(b=4, a=6))
print(keyword_function())


def mf(a, b=2, c=3):
    return a + b + c


# mf(b=4,c=5)

print(mf(1, b=4, c=5))
print(mf(1, 3, 17))


def many(*args, **kwargs):
    print(args)
    print(kwargs)


many(1, 2, 3, gitr=['efdf', 34, 23], name='Mike', job="dfkhkh")


def function_a():
    global a
    a = 1
    b = 2
    return a + b


def function_b():
    c = 243
    return a + c


print(function_a())
print(function_b())


def func1(a, b):
    def inner_func(x):
        return x ** 3

    return inner_func(a) + inner_func(b)


print(func1(4, 5))


def square(x):
    #return list(x * 4, x ** 2, x ** 3)
    z=[]
    z.append(x*4)
    z.append(x**3)
    print(tuple(z))
square(3)

import math
def squarez(a):
    p=a*4
    s=a**2
    d=math.sqrt(2)*a
    return p,s,d
print(squarez(int(input('input squre:\n'))), type(squarez))

