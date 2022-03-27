# x=int(input('7-digit number: '))
# ss=str(x)
# list2=ss.split(' ')
# print(list2)
#

a=int(input())
a=str(a)
b=0
c=0
for i in a:
    i=int(i)
    if i%2==0:
        b+=1
    else:
        c+=1

d=0
if b>c:
    for i in a:
        i=int(i)
        d+=i
    else:
        print(int(a[0])*int(a[3])*int(a[5]))
