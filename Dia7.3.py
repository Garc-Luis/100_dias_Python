from random import choice
word_list = ["aardvark", "baboon", "camel"]
chosen_word = choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use un bucle while para permitir que el usuario adivine nuevamente.
#El ciclo solo debe detenerse una vez que el usuario haya adivinado todas las letras en la palabra_elegida y 'display' no tenga más espacios en blanco ("_").
#Entonces puedes decirle al usuario que ha ganado.
end_of_game = False

while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print('You Win!!')