a=[5,[1,2],2,'r',4,'ee']
b=[4,'we','ee',3,[1,2]]


list1=[]
for i in a:
    if i in b:
        list1.append(i)
print(list1)