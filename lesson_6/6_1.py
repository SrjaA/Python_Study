mas_1=[1,5,3,5,1,100,20,110,100]
mas_2=[]

for i in mas_1:
    if mas_1.count(i)>=2 and i not in mas_2:
        mas_2.append(i)
print(mas_2)