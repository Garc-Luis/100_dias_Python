from High_lower_data import data
from random import choice
from High_lower_logos import logo, vs

while True:
    lives = 5
    dataA = choice(data)
    print(logo)
    print(f'Compare A:  {dataA["name"]}, a {dataA["description"]}, from {dataA["country"]}')
    print(vs)
    dataB = choice(data)
    print(f'Against B:  {dataB["name"]}, a {dataB["description"]}, from {dataB["country"]}')
    election = str(input('Who has more followers? Type "A" or "B"')).lower().strip()
    if election == "a" and dataA['follower_count'] > dataB['follower_count']:
        print('You Win')
    elif election == "a" and dataA['follower_count'] < dataB['follower_count']:
        print('You Lose')
    elif election == "b" and dataA['follower_count'] > dataB['follower_count']:
        print('You Lose')
    elif election == "b" and dataA['follower_count'] < dataB['follower_count']:
        print('You Win')
