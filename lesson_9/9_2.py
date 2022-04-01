words=dict()
count=int(input('Кол-во слов в словаре'))

i=0
while i<count:
    print('Ввод слов: ')
    wrd=str(input('Слово: '))
    value=int(input('Значение: '))
    if wrd not in words:
        words[wrd]=value
    i+=1
print(words)

Numbers=dict(zip([1,2,3],['One','Two','Three']))
print(Numbers)

#цикл for для словаря!!!!!!!!!!!!!!!!!!
Months={1:'dglk',2:'erlkjэ',3:'34ljrf'}

for mn in Months:
    print(mn,': ', Months[mn])

