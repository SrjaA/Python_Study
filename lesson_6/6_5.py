import random

alien_number = random.randint(1, 10)
alien_color = random.randint(1, 2)
print(alien_number, alien_color)

i = 0
while i <= 5:
    user_number = int(input('Enter number (from 1 to 10): '))
    user_color = int(input('Enter color number (1 - Red, 2 - Black): '))
    if 1 <= user_number <= 10 and 1 <= user_color <= 2:
        if alien_number == user_number and alien_color == user_color:
            print("{:*^79}".format(' You WIN! '), end='\n')
            if alien_color == 1:
                print('WIN combination - ', alien_number, 'Red')
            else:
                print('WIN combination - ', alien_number, 'Black')
            break
        else:
            print()
    else:
        print('!!!_Wrong number_!!!')
    i += 1
    print("{:/^79}".format(" Don't worry, Try again! "), end='\n')

else:
    if alien_color == 1:
        print('WIN combination - ',alien_number,'Red')
    else:
        print('WIN combination - ',alien_number,'Black')
