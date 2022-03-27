a=input()
b=''
for i in a:
    if i.isdigit():
        b+=i
    elif b!='':
        print(b)
        b=''
if b!='':
    print(b)