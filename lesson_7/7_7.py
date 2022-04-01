k=int(input('number'))
arr=[]
for i in range(k-1):
    c=int(input('c'))
    arr.append(c)
print(arr)
n=int(input('number'))
pos=int(input('pos'))
arr.insert(pos,n)
print(arr)