with open('number.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    print(lines)
for i in lines:
    i=i.replace('_',' ')
l=i.split(' ')
print(l)
# f = open('numberz.txt', 'r')
# z = f.readlines()
# print(z)
# sar=[]
# for x in z:
#     x=x.replace(r'\n','_')
#     sar.append(x)
# print(sar)