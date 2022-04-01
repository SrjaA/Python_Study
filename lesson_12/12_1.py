f = open('example.txt', 'r')
print(*f)
print(f,type(f))
f.close()

with open('example.txt') as f:\
    print(f.read(7))
    print(*f)


