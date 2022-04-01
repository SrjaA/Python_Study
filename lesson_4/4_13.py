for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i*j:3}', end=' ')
    print()

a=int(input())
b=int(input())
for i in range(a,b+1):
    if a<b:
        print(i)
    else:
        print(10-i)
print()