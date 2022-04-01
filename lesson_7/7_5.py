a=int(input('width: '))
b=int(input('height: '))
c=input('*')
d=input('_')

print(c*a)
for i in range(1,b-2):
    print(c+d*(b-2)+c)
print(c*a)
