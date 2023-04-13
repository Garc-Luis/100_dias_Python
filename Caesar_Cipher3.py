alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine las funciones de encriptar() y desencriptar() en una sola función llamada caesar().
def caesar(tetxs, shifts, directions):
  cipher_text = ""
  if directions == "decode":
    shifts *= -1
  for i in tetxs:
    position = alphabet.index(i)
    new_position = position + shifts
    cipher_text += alphabet[new_position]
  print(f"Here´s the {directions}d result: {cipher_text}")



#TODO-2: Llame a la función caesar(), pasando los valores de 'texto', 'cambio' y 'dirección'.
caesar(text, shift, direction)