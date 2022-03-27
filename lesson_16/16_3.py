def func(x):
    if -5<=x<=5:
        return x*x
    elif x<-5:
        return 2*abs(x)-1
    else:
        return 2*x

for i in range(-10,11):
    print(func(i),end=' ')
