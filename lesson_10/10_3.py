# import random
#
# pics = (0, 1, 2, 3, 4, 5, 6)
# pieces = list(pics)
# print(pieces)
# print(pieces[1:4])
# c = [random.randint(0, 100) for i in range(20)]
# print(c)
# print(c[0])
# print(c[-4])
# pieces.append('sdf')
# pieces.append(56)
# pieces.insert(5, '45')
# pieces[2] = 34
# del pieces[1:3]
# d = list(pieces)
# pieces.remove(56)
# d.extend(pieces)
#
# print(d, pieces)

string='python java javascript c c++ ruby php react'
print(string)
words=string.split()
print(words)
id_longest=0
c=0
for i in words:
    if len(words)<len(words[c]):
        id_longest=c
    c+=1
print(id_longest,c)