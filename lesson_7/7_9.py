s = input()
t = ''
i = 0
for i in range(len(s)):
    if s[i].islower() is False:
        continue
    t = t + s[i]
print(t)

s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = t + s[i]
print(t)