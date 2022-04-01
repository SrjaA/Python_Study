a=int(input())
b=int(input())
c=int(input())

if a<b and b<c:
    print(a,'<',b,'<',c)
elif b>c and c>a:
    print(a,'<',c,'<',b)
else: print(b,'<',a,'<',c)