alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from Caesar_Cipher_Logo import logo

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

        # TODO-3: ¿Qué sucede si el usuario ingresa un número/símbolo/espacio?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
         # end_text = "•••• •• •• 3"
    print(f"Here's the {cipher_direction}d result: {end_text}")
        #continuar = str(input('You want to continue: Yes/No')).lower().strip()
        #if continuar in 'no':
            #break


# TODO-1: Importe e imprima el logotipo de art.py cuando se inicie el programa.
print(logo)

# TODO-4: ¿Puede encontrar una manera de preguntarle al usuario si desea reiniciar el programa de cifrado?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-2: ¿Qué sucede si el usuario ingresa un turno que es mayor que el número de letras del alfabeto?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).
shift = shift % 26
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)