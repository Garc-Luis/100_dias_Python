def soma(valor1, valor2):
    suma = valor1 + valor2
    return  suma


def sustraçao(valor1, valor2):
    resta = valor1 - valor2
    return resta


def multiplicaçao(valor1, valor2):
    multiplicar = valor1 * valor2
    return multiplicar


def diviçao(valor1, valor2):
    dividir = valor1 / valor2
    return dividir

print('*'*15,'Calculadora em Python', '*'*15)
print('Selecione o numero da operaçao desejada:\n\n1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão.')
opção = int(input('Digite a sua Opção (1/2/3/4): '))
print()
num1 = int(input('Digite o primeiro Numero: '))
num2 = int(input('Digite o primeiro Numero: '))
print()
if opção == 1:
    print(f'{num1} + {num2} = {soma(num1, num2)}')
elif opção == 2:
    print(f'{num1} - {num2} = {sustraçao(num1, num2)}')
elif opção == 3:
    print(f'{num1} * {num2} = {multiplicaçao(num1, num2)}')
elif opção == 4:
    print(f'{num1} / {num2} = {diviçao(num1, num2)}')
else:
    print('Opção invalida. Por favor tente novamente')