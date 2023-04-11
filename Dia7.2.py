from random import choice

#Step 2

word_list = ["aardvark", "baboon", "camel"]
chosen_word = choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Crear una Lista vacía llamada display.
#Para cada letra en la palabra_elegida, agregue un "_" a 'mostrar'.
#Entonces, si la palabra_elegida era "manzana", la pantalla debería ser ["_", "_", "_", "_", "_"] con 5 "_" representando cada letra para adivinar.
display = list()

for i in chosen_word:
    display.append('_')
print(display)
guess = input("Guess a letter: ").lower()


#TODO-2: - Pasa por cada posición en la palabra_elegida;
#Si la letra en esa posición coincide con 'adivinar', revele esa letra en la pantalla en esa posición.
#p.ej. Si el usuario adivinó "p" y la palabra elegida fue "manzana", la pantalla debería ser ["_", "p", "p", "_", "_"].
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

#TODO-3: - Imprima 'display' y debería ver la letra adivinada en la posición correcta y todas las demás letras reemplazadas con "_".
#Sugerencia: no se preocupe por hacer que el usuario adivine la siguiente letra. Abordaremos eso en el paso 3.
print(display)