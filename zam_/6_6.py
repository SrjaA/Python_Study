# s=input()
# i=0
# t=0
# z=0
# print(len(s))
# while i<(len(s)-1):
#     if (s[i]+s[i+1]).islower() is True:
#         t+=1
#     elif (s[i]+s[i+1]).isupper():
#         z+=1
#     i+=1
# print(t,z)

a=input()
b=''
x=0
for i in a:
    if i.islower():
        b+=i
        if len(b)==2 or len(b)%2==0:
            x+=1
    elif b!='':
        b=''