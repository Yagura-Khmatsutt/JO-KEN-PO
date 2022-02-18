from random import randint
from time import sleep

print('\33[33m{:=^60}' .format('JO KEN PO'))

print('''\33[34mChoose the following options
[0] ROCK 
[1] PAPER
[2] SCISSORS
''')
print('\33[34m=-' * 30)

player = int(input('\33[36mWhich will you choose?'))

iA = randint(0, 2)
intens = [0, 1, 2]

print('\33[33m opponent will play...')


print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(0.5)
print(intens)

if iA == 0:
    if player == 0:
        print('A TIE')
    elif player == 1:
        print('IT WON')
    elif player == 2:
        print('\33[31mGAME OVER')
    else:
        print('\33[31m//ERROR [number invalid!]')
elif iA == 1:
    if player == 0:
        print('\33[31mGAME OVER')
    elif player == 1:
        print('A TIE')
    elif player == 2:
        print('IT WON')
    else:
        print('\33[31m//ERROR [number invalid!]')

elif iA == 2:
    if player == 0:
        print('IT WON')
    elif player == 1:
        print('\33[31mGAME OVER')
    elif player == 2:
        print('A TIE')
    else:
        print('\33[31m//ERROR [number invalid!]')
#print('Start again?')
