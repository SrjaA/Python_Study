b_d = int(input('Enter your Birthday: '))
b_m = int(input('Enter your Month of Birth: '))

if (0 < b_d <= 20 and b_m == 1) or (20 < b_d <= 31 and b_m == 12):
    print('Capricorn')
elif (0 < b_d <= 20 and b_m == 2) or (20 < b_d <= 31 and b_m == 1):
    print('Aquarius')
elif (0 < b_d <= 20 and b_m == 3) or (20 < b_d <= 31 and b_m == 2):
    print('Pisces')
elif (0 < b_d <= 20 and b_m == 4) or (20 < b_d <= 31 and b_m == 3):
    print('Aries')
elif (0 < b_d <= 20 and b_m == 5) or (20 < b_d <= 31 and b_m == 4):
    print('Taurus')
elif (0 < b_d <= 20 and b_m == 6) or (20 < b_d <= 31 and b_m == 5):
    print('Gemini')
elif (0 < b_d <= 20 and b_m == 7) or (20 < b_d <= 31 and b_m == 6):
    print('Cancer')
elif (0 < b_d <= 20 and b_m == 8) or (20 < b_d <= 31 and b_m == 7):
    print('Leo')
elif (0 < b_d <= 20 and b_m == 9) or (20 < b_d <= 31 and b_m == 8):
    print('Virgo')
elif (0 < b_d <= 20 and b_m == 10) or (20 < b_d <= 31 and b_m == 9):
    print('Libra')
elif (0 < b_d <= 20 and b_m == 11) or (20 < b_d <= 31 and b_m == 10):
    print('Scorpio')
elif (0 < b_d <= 20 and b_m == 12) or (20 < b_d <= 31 and b_m == 11):
    print('Saggitarius')

else:
    print()
    print('Wrong date!')
