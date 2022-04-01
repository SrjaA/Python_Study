a=int(input())
b=str(a)
s=b[::-1]
print(s)

a=int(input('insert number'))
b=0
while a>0:
    b=(b*10)+a%10
    a=a//10
print(b)