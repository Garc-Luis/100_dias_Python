from Dia9_logo import logo

print(logo)
auctions = {}
while True:
    name = str(input('What is your name?: ')).strip()
    bid = float(input('What´s your bid?: $ '))
    auctions[name] = bid
    continuar = str(input('Are there any other Bidders? Type "Y/Yes" or "N/No"')).upper()
    if continuar in "N":
        break
mayor = 0
ganador = ""
for i in auctions:
    monto_mayor = auctions[i]
    if monto_mayor > mayor:
        mayor = monto_mayor
        ganador = i
print(f'The winner is {ganador} with a bid of ${mayor:.2f}')