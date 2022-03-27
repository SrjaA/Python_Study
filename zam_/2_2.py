# list1 = ['а', 'о', 'и', 'е', 'ы', 'ю', 'я', 'у', 'ё']
# list2 = []
# s = input('enter text: ')
# t = 0
# for k in range(len(s)):
#     if s[k] in list1:
#         t = t + 1
#         list2.append(s[k])
#     k = +1
# z = len(s) - t
# print(t, z)
# if z == t:
#     print(list2)

#
text=input('')
glasn=0
soglasn=0
a=[]
for i in text:
    if i in 'aoeyiu':
        glasn+=1
        a.append(i)
    else:
        soglasn+=1
print(glasn,soglasn)
print(a)
