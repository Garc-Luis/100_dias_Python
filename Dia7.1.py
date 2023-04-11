from random import choice

#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Elija aleatoriamente una palabra de la lista de palabras y asígnela a una variable llamada palabra_elegida.

chosen_word = choice(word_list)
#TODO-2 - Pide al usuario que adivine una letra y asigne su respuesta a una variable llamada adivinar. Hacer conjetura en minúsculas.
print(chosen_word)
guess = str(input('Guess a letter?')).lower()
#TODO-3 - Comprobar si la letra que el usuario adivinó (adivinar) es una de las letras de la palabra_elegida.vxçxççx
for i in range(len(chosen_word)):
    if guess in chosen_word[i]:
        print("Right")
    else:
        print("Wrong")