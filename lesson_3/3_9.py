s='Missisipi is the longest river of Nothern America'
print(s)
# Third character of the string
print(s[2])
# Penultimate
print(s[-2])
# First five characters
print(s[0:4].ljust(49,'.'))
# without two last characters
print(s[0:-2])
# even characters
print(s[0::2])
# uneven
print(s[1::2])
# in reverse
print(s[::-1])
print(s[45:3:-3])
# in reverse through one
print(s[::-2])
# length
print('String length -',len(s),'characters\n', type(s))
