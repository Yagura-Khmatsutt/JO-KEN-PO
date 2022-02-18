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

if iA == 0:
    if player == 0:
        print('A TIE')
    elif player == 1:
        print('IT WON')
    elif player == 2:
        print('GAME OVER')
    else:
        print('\33[31m//ERROR [number invalid!]')
elif iA == 1:
    if player == 0:
        print('GAME OVER')
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
        print('GAME OVER')
    elif player == 2:
        print('A TIE')
    else:
        print('\33[31m//ERROR [number invalid!]')
#print('Start again?')
