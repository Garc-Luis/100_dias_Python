############### Proyecto de Blackjack ####################

#Dificultad Normal 😎: Usa todos los Consejos a continuación para completar el proyecto.
#Dificultad Difícil 🤔: Usa solo las Pistas 1, 2, 3 para completar el proyecto.
#Dificultad Extra Difícil 😭: solo usa las pistas 1 y 2 para completar el proyecto.
#ExpertoDificultad 🤯: Usa solo la Pista 1 para completar el proyecto.

############### Nuestras reglas de la casa de Blackjack ####################

## El mazo tiene un tamaño ilimitado.
## No hay bromistas.
## La jota, la reina y el rey cuentan como 10.
## El As puede contar como 11 o 1.
## Utilice la siguiente lista como mazo de cartas:
## cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## Las cartas de la lista tienen la misma probabilidad de ser extraídas.
## Las cartas no se eliminan del mazo a medida que se extraen.
## La computadora es el crupier.

#################### Sugerencias ####################

#Pista 1: Vaya a este sitio web y pruebe el juego de Blackjack:
# https://games.washingtonpost.com/games/blackjack/
#Entonces pruebe el proyecto de Blackjack completo aquí:
# http://blackjack-final.appbrewery.repl.run

#Pista 2: Lea este desglose de los requisitos del programa:
# http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Luego intente crear su propio diagrama de flujo para el programa.

#Pista 3: descarga y lee este diagrama de flujo que he creado:
#https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Pista 4: Cree una función deal_card() que use la Lista a continuación para *devolver* una carta al azar.
#11 es el As.
#cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Pista 5: Reparte 2 cartas al usuario y a la computadora usando deal_card() y append().
#tarjetas_de_usuario = []
#computer_cards = []

#Pista 6: Cree una función llamada calcule_score() que tome una Lista de tarjetas como entrada
#y devuelve la puntuación.
#Busque la función sum() para ayudarlo a hacer esto.

#Pista 7: Dentro de compute_score() comprueba si hay un blackjack (una mano con solo 2 cartas: as + 10) y devuelve 0 en lugar de la puntuación real. 0 representará un blackjack en nuestro juego.

#Pista 8: Dentro de la función de calcular_puntuación() comprueba si hay un 11 (as). Si el puntaje ya supera los 21, elimine el 11 y reemplácelo con un 1. Es posible que deba buscar append() y remove().

#Pista 9: Llame a compute_score(). Si la computadora o el usuario tiene un blackjack (0) o si la puntuación del usuario es superior a 21, el juego termina.

#Pista 10: Si el juego no ha terminado, pregunta al usuario si quiere robar otra carta. En caso afirmativo, utilice la función deal_card() para agregar otra tarjeta a la Lista de tarjetas de usuario. Si no, entonces el juego ha terminado.

#Pista 11: La puntuación deberá volver a comprobarse con cada nueva carta extraída y las comprobaciones de la Pista 9 deberán repetirse hasta que finalice el juego.

#Pista 12: Una vez que el usuario haya terminado, es hora de dejar que la computadora juegue. La computadora debe seguir sacando cartas siempre que tenga una puntuación inferior a 17.

#Pista 13: Cree una función llamada compare() y pase el user_score y el computer_score. Si la computadora y el usuario tienen la misma puntuación, entonces es un empate. Si la computadora tiene un blackjack (0), entonces el usuario pierde. Si el usuario tiene un blackjack (0), entonces el usuario gana. Si el user_score es superior a 21, el usuario pierde. Si computer_score es superior a 21, entonces la computadora pierde. Si ninguno de los anteriores, gana el jugador con la puntuación más alta.

#Pista 14: Pregúntale al usuario si quiere reiniciar el juego. Si responde que sí, borre la consola y comience un nuevo juego de blackjack y muestre el logotipo de art.py.