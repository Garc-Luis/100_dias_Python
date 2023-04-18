from random import choice
from Black_Jack_Logo import logo

def barajo():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card

def total(card):
    if sum(card) == 21 and len(card) == 2:
        return 0
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)


def resultado(usuario_score, computer_score):
        if usuario_score > 21 and computer_score > 21:
            return "You went over. You lose 😤"
        if usuario_score == computer_score:
            return "Draw 🙃"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif usuario_score == 0:
            return "Win with a Blackjack 😎"
        elif usuario_score > 21:
            return "You went over. You lose 😭"
        elif computer_score > 21:
            return "Opponent went over. You win 😁"
        elif usuario_score > computer_score:
            return "You win 😃"
        else:
            return "You lose 😤"

def blackjack_game():
    print(logo)
    usuario_card = []
    computer_card = []
    for i in range(2):
        usuario_card.append(barajo())
        computer_card.append(barajo())
    while True:
        usuario_score = total(usuario_card)
        computer_score = total(computer_card)
        print(f'Your Cards : {usuario_card}, current score: {usuario_score}')
        print(f'Computer´s first card: {usuario_card[0]}')
        if usuario_score == 0 or computer_score == 0 or usuario_score >21:
            break
        else:
            usuario_should = str(input('Type "y" to get another card, type "n" to pass: '))
            if usuario_should == "y":
                usuario_card.append(barajo())
            else:
                break
    while computer_score != 0 and computer_score < 17:
        computer_card.append(barajo())
        computer_score = total(computer_card)
    print(f'Your final hand: {usuario_card}, final score: {usuario_score}')
    print(f'Computer´s final hand: {computer_card}, final score: {computer_score}')
    print(resultado(usuario_score, computer_score))




while True:
    play_to_Game = str(input('Do you wnat to play a game of BlackJack? Type "y" or "n": ')).lower().strip()
    if play_to_Game in "Yy":
        blackjack_game()
    else:
        break
