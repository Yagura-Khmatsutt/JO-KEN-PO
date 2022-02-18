from random import randint
from time import sleep

print('\33[33m{:=^60}' .format('JO KEN PO'))

opponentWillPlay = randint(0, 2)
itens = ['ROCK', 'PAPER', 'SCISSORS']

print('''\33[34mChoose the following options
[0] ROCK 
[1] PAPER
[2] SCISSORS
''')
print('\33[34m=-' * 30)

player = int(input('\33[36mWhich will you choose?'))

print('\33[33m Opponent will play...')

print('\33[32mJO')
sleep(1)
print('\33[34mKEN')
sleep(1)
print('\33[36mPO!!')
sleep(0.5)

print('You chose {}'.format(itens[player]))
print('Opponent will play {}'.format(itens[opponentWillPlay]))

if opponentWillPlay == 0:
    if player == 0:
        print('A TIE')
    elif player == 1:
        print('\33[34mYOU WIN')
    elif player == 2:
        print('\33[31mGAME OVER')
    else:
        print('\33[31m//ERROR [number invalid!]')
elif opponentWillPlay == 1:
    if player == 0:
        print('\33[31mGAME OVER')
    elif player == 1:
        print('A TIE')
    elif player == 2:
        print('\33[34mYOU WIN')
    else:
        print('\33[31m//ERROR [number invalid!]')

elif opponentWillPlay == 2:
    if player == 0:
        print('\33[34mYOU WIN')
    elif player == 1:
        print('\33[31mGAME OVER')
    elif player == 2:
        print('A TIE')
    else:
        print('\33[31m//ERROR [number invalid!]')
#print('Start again?')
