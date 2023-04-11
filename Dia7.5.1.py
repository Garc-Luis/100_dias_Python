#Step 5

import random
from Hangman_words import word_list
from Stages import stages, logo

#TODO-1: - Actualice la lista de palabras para usar la 'word_list' de hangman_words.py
#Borrar esta línea: word_list = ["ardvark", "babuino", "camello"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Importa el logo de hangman_art.py e imprímelo al comienzo del juego.

print(logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')
print()
#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # TODO-4: - Si el usuario ha ingresado una letra que ya ha adivinado, imprima la letra y avísele.
    if guess in display:
        print(f'[{guess}], This letter is already inside the word')
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - Si la letra no está en la palabra_elegida, imprime la letra y hazles saber que no está en la palabra.
        print(f'[{guess}] This letter is not in the word, You lose a live')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Importa los escenarios desde hangman_art.py y haz que este error desaparezca.
    print(stages[lives])