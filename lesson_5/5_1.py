# a=input('')
# b=a.find(' ')
# print(a[b:],a[0:b])

arr = [1, 3, 4, 9, 13]
l = len(arr)
print(arr, 'Длина:', l, type(arr))

for i in arr:
    print(i, end=' ')
    if i == 9:
        break
print()
for i in arr:
    if i == 9:
        continue
    print(i, end=' ')
print()
arr.append(300)
print(arr)

i=1
while i<10:
    print(i**2, end=' ')
    i+=1
print()
