num_set = {2, 3, 4, 5, 6, 7, 8, 9}
print(type(num_set))
string_set = {'dfkj', 'fgkjfg', 'kjdfgkj', 'dfgkjke3'}
print(string_set)
num_set = set[1, 2, 3, 4, 5, 6,'dfkj']
num_set2 = {1, 2, 3, 1, 2}
print(num_set2)
num_set.add('feb')

print(num_set)
num_set.discard(3)
print(num_set)
num_set.remove('feb')
print(num_set)
all = string_set.union(num_set)
print(all)
print(string_set | num_set)

x={1,2,3}
y={4,3,6}
print(x&y)
A={1,2,3}
B={4,3,6}
print(A-B)
print(B-A)
v=A.isdisjoint(B)
print(v)

h=[1,2,2,3,5,4,5,5]
f=list(set(h))
if len(f)!=len(h):
    print('mg')