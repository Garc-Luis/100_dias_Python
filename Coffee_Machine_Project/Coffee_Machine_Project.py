from Money_maker import MoneyMachine
from menu import Menu, MenuItem
from Coffee_Maker import CoffeeMaker

registradora = MoneyMachine()
cafetera = CoffeeMaker()
menu = Menu()

while True:
    opciones = menu.get_items()
    eleccion = str(input(f'What would you like? {opciones}: ')).strip().lower()
    if eleccion == "off":
        break
    elif eleccion == "report":
        cafetera.report()
        registradora.report()
    else:
        cafe = menu.find_drink(eleccion)
        if cafetera.is_resource_sufficient(cafe):
            if registradora.make_payment(cafe.cost):
                cafetera.make_coffee(cafe)