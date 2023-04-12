alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Cree una función llamada 'cifrar' que tome el 'texto' y el 'cambio' como entradas.
def encrypt(texts, shifts):
    text_encryp = []
    for i in texts:
        position = alphabet.index(i)
        new_position = position + shifts
        new_letter = alphabet[new_position]
        text_encryp += new_letter
    print(f'The encode text is {"".join(text_encryp)}')


    #TODO-2: Dentro de la función 'encriptar', desplaza cada letra del 'texto' hacia adelante en el alfabeto por la cantidad de desplazamiento e imprime el texto encriptado.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Llame a la función de cifrado y pase las entradas del usuario. Debería poder probar el código y cifrar un mensaje.
encrypt(text, shift)