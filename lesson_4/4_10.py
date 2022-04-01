# Create string
my_string = 'Mission impossible'
print(my_string)
# String division
my_string_1 = my_string[:7]
my_string_2 = my_string[8:]

# Create new string

print(my_string_2, my_string_1)

# or
# x=my_string.split(' ')
# print(x[1], x[0])
a,b=map(str,my_string.split())
print(b,a)
i = 1
for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
    print('#', i, ' color of rainbow is ', color, sep='')
    i += 1


m = 1


#help(print)
#help(str)