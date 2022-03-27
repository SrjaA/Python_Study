with open('xyz.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    print(lines)
v=0
c=[]
for i in lines:
    v+=1
    c.append(len(i))
print(v,c)


f=open('xyz.txt')
line=0
for i in f:
    line+=1
    print(i,len(i),'симв')
print(line,'стр.')
f.close()