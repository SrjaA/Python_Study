m = 1
for i in range(1, 100, 2):
    m *= i
print(m)

for i in range(1, 100, 2):
    i *= i
print(i)

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i*j:3}', end=' ')
    print()
