from Calculator_logo import logo


#Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return  n1 / n2

operations = {
    "+" : add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = int(input("What is the first number?: "))
    for i in operations:
        print(i)

    while True:
        operattor = str(input("Pick another operation: "))
        num2 = int(input("What's the next number?: "))
        calc = operations[operattor]
        answer = calc(num1, num2)
        print(f'{num1} {operattor} {num2}: {answer}')
        continuar = str(input(f"Type 'Y' to continue calculating with {answer}, or type 'n' to exit.: ")).lower().strip()
        if continuar in 'n':
            break
            calculator()
        else:
            num1 = answer

calculator()