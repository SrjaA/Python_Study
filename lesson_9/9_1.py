d = {}
d = {'dict': 1, 'dictionary': 2}
print(d)
print(type(d))

d = dict(short='dict', long='dictionary')
d_2 = dict([(1, 1), (2, 4)])
print(d, '\n', d_2)

d=dict.fromkeys(['a','b'])
d_2=dict.fromkeys(['a','b'],100)
print(d, '\n', d_2)

d={a:a**2 for a in range(7)}
print(d)
d={1:2,2:4,3:9}
d[4]=4**2
print(d[1])
print(d)
print(d.items())