import this

arr = [1, 2, 3, -4, 5, 6, -7, 8, 9, 10]
sum = 0
mult = 1
for i in arr:
    sum += i
    mult *= i
print(sum, mult, sep='_/\_')

max_num=0
for i in arr:
    if i>max_num:
        max_num=i
print(max_num)

for i in arr:
    if i<max_num:
        max_num=i
print(max_num)

# i=0
# while i<10:
#     print(i, end='  ')
#     i+=1
# print()

i=1
while i<10:
    print(i**2, end=' ')
    i+=1
print()