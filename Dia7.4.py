#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Crear una variable llamada 'vidas' para realizar un seguimiento de la cantidad de vidas restantes.
#Establecer 'vidas' en 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # TODO-2: - Si adivinar no es una letra en la palabra_elegida,
    # Entonces reduce las 'vidas' en 1.
    # Si las vidas llegan a 0, entonces el juego debería detenerse y debería imprimirse "Tú pierdes".
    if guess not in chosen_word:
        print('No Macht')
        lives -=1
        if lives == 0:
            end_of_game = True
            print('You lose')

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - imprime el arte ASCII de 'etapas' que corresponde al número actual de 'vidas' que le quedan al usuario.
    print(stages[lives])