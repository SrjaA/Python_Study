d = dict(name='Valik', age='56',city='California')
print(d)
print(d['age'])

d={'BMW':['X5','M6','z4'],'Tesla':['modelX','modelS']}
d=dict(BMW=['X5','M6','z4'],Tesla=['modelX','modelS'])
print(d['BMW'][2])

d1={"a":100,"b":200,"c":300}
d2={"a":300,"b":200,"d":400}
print(d1["b"]==d2["b"])

d={1:2,2:5,4:13}
l=1
for i in d:
    l*=d[i]
    #l=l*d[i]
print(l)
print(d[4])

l1=[1,2,3]
l2=[4,5,6]
d=dict(zip(l1,l2))
print(d)

s='pythonist'
d={i:s.count(i) for i in s}
print(d)
