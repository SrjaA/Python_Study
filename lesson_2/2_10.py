import random
print()
print("{:*^79}".format(' Hi! Welcome to lottery "5 of 36" '))
print()

user_input_1 = int(input('Enter first number (1 to 36): '))
user_input_2 = int(input('Enter second number (1 to 36): '))
user_input_3 = int(input('Enter third number (1 to 36): '))
user_input_4 = int(input('Enter fourth number (1 to 36): '))
user_input_5 = int(input('Enter fifth number (1 to 36): '))
#user_input_6 = int(input('Enter sixth number (1 to 36): '))


random_input_1 = random.randint(1, 36)
random_input_2 = random.randint(1, 36)
random_input_3 = random.randint(1, 36)
random_input_4 = random.randint(1, 36)
random_input_5 = random.randint(1, 36)
#random_input_6 = random.randint(1, 36)

print(
    "%15s%5d%5d%5d%5d%5d" % ('Your combination', user_input_1, user_input_2, user_input_3, user_input_4, user_input_5))
print("%16s%5d%5d%5d%5d%5d" % (
'WON combination', random_input_1, random_input_2, random_input_3, random_input_4, random_input_5))
