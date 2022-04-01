string = 'python,JS! C?'
st = {',', '!', '?'}
words = string.split()

i = 0
for word in words:
    if word[-1] in st:
        words[i] = word[:-1]
        word = words[i]
    if word[0] in st:
        words[i] = word[1:]
    i += 1
for i in words:
    print(i, end=' ')
print()
