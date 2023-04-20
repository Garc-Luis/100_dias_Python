from random import randint

easy = 10
hard = 5

def dificulty():
    print('Welcome to the Number Guessing Game')
    print('I´m thinking of a number between 1 and 100')
    dificult = str(input('Choose a difficulty. Type "Easy" or "Hard": ')).lower().strip()
    return dificult

def lifes_game(answer, number, live):
    if answer > number:
        print('Too High\nGuess again')
        return live += 1
    elif answer < number:
        print('Too Low\nGuess again')
        return live += 1
    else:
        print(f'You got it! The answer was {answer}')


def number_guessing_game(dificulty):
    number= randint(1, 101)






number_guessing_game(dificulty())