list=[15,48,'hello',62,19,'world']
list1=[]
for x in list:
    list1.append(x)
    if type(x) is int and x%2==0:
        x1=str(x)
        x_sum=int(x1[0])+int(x1[1])
        list1.append(x_sum)
        x+=1
print(list1)
list1.pop(3)
print(list1)