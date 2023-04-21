from High_lower_data import data
from random import choice
from High_lower_logos import logo, vs


def high_lower_game():
    print(logo)
    score = 0
    dataA = choice(data)
    dataB = choice(data)
    game = True
    while game:
        dataA = dataB
        dataB = choice(data)
        while dataA == dataB:
            dataB = choice(data)
            print(f'Compare A:  {dataA["name"]}, a {dataA["description"]}, from {dataA["country"]}')
            print(vs)
            print(f'Against B:  {dataB["name"]}, a {dataB["description"]}, from {dataB["country"]}')
            election = str(input('Who has more followers? Type "A" or "B": ')).lower().strip()
            if election == "a" and dataA['follower_count'] > dataB['follower_count']:
                print('You Win')
                score +=1
                print(f'You´re right! Current score: {score}')
            elif election == "a" and dataA['follower_count'] < dataB['follower_count']:
                print('You Lose')
                print(f'Sorry, that´s wrong. Final Score {score}')
                game = False
            elif election == "b" and dataA['follower_count'] > dataB['follower_count']:
                print('You Lose')
                print(f'Sorry, that´s wrong. Final Score {score}')
                game = False
            elif election == "b" and dataA['follower_count'] < dataB['follower_count']:
                print('You Win')
                score += 1
                print(f'You´re right! Current score: {score}')

high_lower_game()