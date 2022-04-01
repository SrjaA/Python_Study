s=input()




print(s[:s.find('h')+1]+s[s.find('h')+1:s.rfind('h')].replace('h','H')+s[s.rfind('h'):])
#
s=input()
t=''
for i in range(len(s)):
    if i%3!=0:
        t=t+s[i]
print(t)
#
s=input()
print(s[:s.find('h')]+s[s.rfind('h')+1:])
#
s=input()
ss=s[s.rfind('h'):s.find('h'):-1]
print(s[:s.find('h')]+ss+s[s.rfind('h'):])
#

s = input()
ss = s[s.find('f') + 1:len(s)]
if s.count('f') == 1:
    print('-1')
elif s.count('f') == 0:
    print('-2')
else:
    print(ss.find('f') + (s.find('f') + 1))
#
s = input()
l = int(len(s))
if l % 2 == 0:
    print(s[l // 2:] + s[0:l // 2])
else:
    print(s[l // 2 + 1:] + s[0:l // 2 + 1])
l = s.find(' ')
print(s[l + 1:], s[0:l])
#
i = 0
sum = 0
while True:
    j = int(input())
    if j == 55:
        break
    sum += j
    i += 1
print(i)
print(sum)
print(round(sum / i))

s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') > 1:
    print(s.find('f'), s.rfind('f'))
else:
    print()

import random

my_list = ['яблоко', 'банан', 'вишня', 'персик']

for c, value in enumerate(my_list, 1):
    print(c, value)

# Результат:
# 1 яблоко
# 2 банан
# 3 вишня
# 4 персик
print(len(my_list))
i = 0
while i < len(my_list) - 2:
    my_list[i] = my_list[i] + '22'
    i = i + 1
print(my_list)

lists = []
for i in range(7):
    c = random.randint(3, 3000)
    lists.append(c)
print(lists)

print(list(range(1, 20, 2)))

numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617,
           865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978,
           328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67,
           104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854,
           685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
numbers2 = []
numbers3 = []
for number in numbers:
    if number % 2 == 0:
        numbers2.append(number)
    if number == 237:
        numbers2.insert(-1, 'why?')
        print(numbers2)
        break

for number in numbers:
    if number == 237:
        break
    if number % 2 == 1:
        continue
    numbers3.append(number)
else:
    print('kaniez')
print(numbers3)

# вычисление суммы элементов списка
# Заданный список
T = [2.8, 3.5, 4.9, 0.01, 2.34]

s = 0
for t in T:
    s = s + t
print("s = ", s)  # s = 13.549999999999999

i = 0
while i != 10:
    if i % 2 == 0:
        print(i)
    i += 2

# number = int(input())
# word = input()
#
# # write a condition for plurals
# if number != 1:
#     #word = word + 's'
#     word.join([word,"def"])
#
# print(number, word)
