from random import randint

def dificulty():
    print('Welcome to the Number Guessing Game')
    print('I´m thinking of a number between 1 and 100')
    dificult = str(input('Choose a difficulty. Type "Easy" or "Hard": ')).lower().strip()
    return dificult


def number_guessing_game(dificulty):
    number_correct = randint(1, 101)
    easy = 10
    life = 0
    hard = 5
    if dificulty == "easy":
        print('You have 10 attempts remaining to guess the number.')
        while life < easy:
            answer = int(input('Make a guess: '))
            life +=1
         if answer == number_correct:
                print(f'You Win!!! The correct number was {number_correct} ')
                break
            elif answer > number_correct:
                print('Too High\nGuess again')
            elif answer < number_correct:
                print('Too Low\nGuess again')
            print(f'You have {easy - life} attempts remaining to guess the number')
    else:
        print('You have 5 attempts remaining to guess the number.')
        while life < hard:
            answer = int(input('Make a guess: '))
            life += 1
            if answer == number_correct:
                print(f'You Win!!! The correct number was {number_correct} ')
                break
            elif answer > number_correct:
                print('Too High\nGuess again')
            elif answer < number_correct:
                print('Too Low\nGuess again')
            print(f'You have {hard  - life} attempts remaining to guess the number')


number_guessing_game(dificulty())