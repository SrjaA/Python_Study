a={35,78,21,37,2,98,6,100,231}
b={45,21,124,76,5,23,91,234}

if sum(a)<sum(b):
    print('Summ Second tuple highly')
else:print('Summ First tuple highly')

print(max(a),max(b))
print(min(a),min(b))

#2
s='An apple a day keeps the doctor away'
z=dict()
d={i:s.count(i) for i in s}
print(d)

#3
c=[2,4,3,5,7,14,13,10]
k=[3,6,4,1,0,13,18,9,91]
v=0
for i in c:
    if i in k:
        v+=1
print(v)

#4
try:
    a=int(input('first number: '))
    b=int(input('second number: '))
    c=a/b
except ZeroDivisionError:
    print('произошла ошибка')
else:
    print('result*2',c**2, type(c**2))
finally:
    print('konec')

violatorsongsdict = {

'World in My Eyes': 4.76,

'Sweetest Perfection': 5.43,

'Personal Jesus': 4.56,

'Halo': 4.30,

'Waiting for the Night': 6.07,

'Enjoy the Silence': 4.6,

'Policy of Truth': 4.88,

'Blue Dress': 4.18,

'Clean': 5.68,

}

#5
print(sum(violatorsongsdict.values()))

