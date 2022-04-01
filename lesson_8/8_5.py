import random

c=tuple(random.randint(0,9) for x in range(9))
print(c)
print(sum(c))

long_word=('n','n','a','i','i','a','i','i','i','n','n','a','i','i','i','i')
print('n',long_word.count('n'),'a',long_word.count('a'),'i',long_word.count('i'),)

week_temp=(26,29,34,32,28,26,23)
sum_temp=sum(week_temp)
days=len(week_temp)
mean_temp=sum_temp/days
print(int(mean_temp))