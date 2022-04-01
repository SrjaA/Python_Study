# Five guys sometimes play poker
# however, they always have a problem getting together
# Zohn can any day of the week, Ivaen can't on Tuesday, Dart can't on Wednesday and Saturday
# Biba and Boba can only know the schedule at the beginning of the week
# Let's help them get together

Zohn = {1, 2, 3, 4, 5, 6, 7}
Ivaen = {1, 3, 4, 5, 6, 7}
Dart = {1, 2, 4, 5, 7}
print(len(Zohn), len(Dart))
Biba = {int(input("Biba's free day: ")) for i in range(4)}
Boba = {int(input("Boba's free day: ")) for x in range(4)}

if Zohn & Ivaen & Dart & Biba & Boba == 0:
    print('you will not to meet')
else:
    print('you will meet - ', Zohn & Ivaen & Dart & Biba & Boba)
