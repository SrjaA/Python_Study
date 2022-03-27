a=['asd','sdfsrrrrdf','efkhkj',2,56,34,23477]
print(a)
b=[]
n=[]
f=open('chb.txt','a')
for i in a:
    if type(i) is str:
        b.append(i)
    elif type(i) is int:
        i=int(i)
        n.append(i)
b.sort(key=len)
n.sort()
for i in b:
    f.write(i+'\n')
for i in n:
    i=str(i)
    f.write(i+'\n')
f.close()