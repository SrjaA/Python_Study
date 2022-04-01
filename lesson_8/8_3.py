a=[4,6,'py','tell',78]
b=[44,'hello',56,'exept',3]

print(a+b)
a.insert(3,6)
print(a)

for i in a:
    if type(i) is str:
        a.remove(i)
a.sort()
print(a)
print(len(a))