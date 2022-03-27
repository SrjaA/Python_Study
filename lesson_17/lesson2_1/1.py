import random

n=2
m=3
A=[]
for i in range(n):
    A.append([0]*m)
print(A)
A=[[1,2,3],[4,5,6]]
print(A)
print(A[1][2])

for i in range(len(A)):
    for y in range(len(A[i])):
        print(A[i][y],end=' ')
    print(end='\n')
A=[[0]*m for i in range(n)]
print(A)
for i in range (n):
    for y in range(m):
        A[i][y]=2
    print(A)

# k = int(input('input n-string'))
# l = int(input('inout g'))
# A = [[0] * k for i in range(l)]
# for i in range(k):
#     for y in range(l):
#         A[i][y] = random.randint(0, 100)
#     print(A)
#
# print(A)

k=int(input('input n-string '))
l=int(input('inout g '))
A=[[0]*k for i in range(l)]
for i in range(1,k+1):
    for y in range(1,k+1):
        if i%2==0:
            print(i,end=' ')
        else:
            print(y,end=' ')
    print()

a=100/0
