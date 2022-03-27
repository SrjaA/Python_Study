# ls=input().split()
#
# for i in ls:
#     if ls.count(i)==1:
#         print(i)
# exit(print('Goodbye'))

#

df=[3, 5, 2, 3, 5, 6, 7,0,1,1]
s=0

for i in df:
    if df.count(i)>1:
        s+=1
    else: continue
print(s)

#


# tpl1=tuple(int(i) for i in input().split())
# print(tpl1)
# ls=input().split()
# ls2=[]
# for i in ls:
#     ls2.append(int(i))
# tpl2=tuple(ls2)
# print(tpl2)
#
# if sum(tpl1)>sum(tpl2):
#     print(f"сумма больше в первом")
# elif sum(tpl1)<sum(tpl2):
#     print(f"сумма больше во втором"

#

# tpl1=tuple(int(i) for i in input().split())
# print(tpl1.index(max(tpl1)))


#

str=input()
dict={}

d={i:str.count(i) for i in str}
print(d)


#

menu={'грибная':["мука, грибы, картошка, лук",5,1200],
       'маргарита':["сыр,мука,яйца",780],
       "борщевая": ["борщевик, свекла, хурма", 3,670]}
pizza=input("Какая пицца интересует? ")
wish=input('Что Вы хотели бы уточнить? ')
for k, v in menu.items():
    if pizza == k:
        if wish == "описание":
            print(f"Пицца {k} состоит из {v[0]}")
        elif wish=='цена':
            print(f"Пицца {k} стоит из {v[1]}")
weight=int(input('сколько положить? '))

print(f"{menu[pizza[1]]*weight/100}")
print(f"{pizza} осталось {menu[pizza][-1] - weight} грамм")

#

lst1=set([int(i) for i in input().split()])
lst2=set([int(i) for i in input().split()])

print(len(lst1-lst2))

#

with open("text.txt","r") as f:
    for line in f:
    line=line.rstrip()
    #for i in line:
    mark=int(line[-1])
    if mark>4:
        print(line[:-1])