with open('numberz.txt') as f:
    s = f.readlines()
    s = [line.strip() for line in s]
    print(s)
    print(2 ** 38)
nums = []
wors = list()
for line in s:
    if line.isdigit() is True:
        nums.append(int(line))
        nums.sort()
    else:
        wors.append(line)
        wors.sort(key=len)
try:
    print(nums + wors)
except Exception:
    print('schota ne tak')
