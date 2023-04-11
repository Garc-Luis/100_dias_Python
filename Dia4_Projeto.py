from random import randint
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇
games = [rock, paper, scissors]
computador = randint(0,2)
jogador = int(input('Type\n[0] for Rock.\n[1] for Paper.\n[2] for Scissors.\nWhat do you choice?: '))

if jogador == 0 and computador == 0:
    print(games[jogador])
    print('Computer Chose:')
    print(games[computador])
    print('Ops! It´s a draw.')
elif jogador == 0 and computador == 1:
    print(games[jogador])
    print('Computer Chose:')
    print(games[computador])
    print('Game Over! You Lose.')
elif jogador == 0 and computador == 2:
    print(games[jogador])
    print('Computer Chose:')
    print(games[computador])
    print('Yes! You WIN.')
if jogador == 1 and computador == 0:
    print(games[jogador])
    print('Computer Chose:')
    print(games[computador])
    print('Yes! You WIN.')
elif jogador == 1 and computador == 1:
    print(games[jogador])
    print('Computer Chose:')
    print(games[computador])
    print('Ops! It´s a draw')
elif jogador == 1 and computador == 2:
    print(games[jogador])
    print('Computer Chose:')
    print(games[computador])
    print('Game Over! You Lose.')
if jogador == 2 and computador == 0:
    print('Game Over! You Lose.')
elif jogador == 2 and computador == 1:
    print(games[jogador])
    print('Computer Chose:')
    print(games[computador])
    print('Yes! You WIN.')
elif jogador == 2 and computador == 2:
    print(games[jogador])
    print('Computer Chose:')
    print(games[computador])
    print('Ops! It´s a draw')
else:
    print('You typed an invalid number, You lose.')
