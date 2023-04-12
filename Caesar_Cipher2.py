alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

#TODO-1: Cree una función diferente llamada 'descifrar' que tome el 'texto' y el 'cambio' como entradas.
def descrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    cipher_text += alphabet[new_position]
  print(f"The decode text is {cipher_text}")
  #TODO-2: Dentro de la función 'descifrar', mueva cada letra del 'texto' *hacia atrás* en el alfabeto por la cantidad de cambio e imprima el texto descifrado.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Compruebe si el usuario desea cifrar o descifrar el mensaje comprobando la variable 'dirección'. Luego llame a la función correcta basada en esa variable de 'dirección'. Debería poder probar el código para cifrar *Y* descifrar un mensaje.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    descrypt(plain_text=text, shift_amount=shift)