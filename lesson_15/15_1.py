def factorial(b):
    if b != 0:
        return b * factorial(b - 1)
    else:
        return 1


print(factorial(5))

product = lambda x, y: x ** y

print(product(2, 256))


def mul(a):
    def helper(b, c):
        return a ** b / c

    return helper


print(mul(3)(2, 2))

def simple_decore(fn):
    print('start func')
    fn()
    print('stop func')
@simple_decore
def first_test():
    print('Test func 1')

@simple_decore
def second_test():
    print('test func 2')


# first_test_wrapped = simple_decore(first_test)
# second_test_wrapped = simple_decore(second_test)

import math
a=9
b=math.sqrt(a)
print(b)
