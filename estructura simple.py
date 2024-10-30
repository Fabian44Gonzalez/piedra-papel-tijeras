def instrucciones():
    print("Vas a jugar a piedra, papel, tijeras.")
    print("Gana el primero en llegr a 3 puntos, tu contrincante es el ordenador. Buena suerte!")


def menu():
    print("0 -> Piedra")
    print("1 -> Papel")
    print("2 -> Tijeras")



def eleccion_jugador():
    jugador = -1

    while jugador <= -1:
        jugador = int(input("Escoge tu elección"))
        if jugador == 0:
            print("Piedra")
        elif jugador == 1:
            print("Papel")
        elif jugador == 2:
            print("Tijeras")
        else:
            print("Escoge un valor correcto")
    return jugador


def eleccion_ordenador():
    import random
    ordenador = random.randint(0, 2) #El ordenador selecciona un numero al azar
    if ordenador == 0:
        print("Piedra")
    elif ordenador == 1:
        print("Papel")
    elif ordenador == 2:
        print("Tijeras")
    return ordenador



def puntuacion ():
    puntos_jugador = 0
    puntos_ordenador = 0

    while puntos_jugador <= 3 or puntos_ordenador <= 3:

        jugador = eleccion_jugador()
        ordenador = eleccion_ordenador()

        if jugador == ordenador:
            print("Empate")
        elif (jugador == 0 and ordenador == 2) | (jugador == 1 and ordenador == 0) | (jugador == 2 and ordenador == 1):
            puntos_jugador += 1 #Se suma en 1 el valor de los puntos del jugador 
            print("Ganaste la ronda")
        else:
            puntos_ordenador += 1 #Se suma en 1 el valor de los puntos del ordenador
            print("Perdiste la ronda")
        
        print("Tus puntos:", puntos_jugador, "Puntos ordenador:", puntos_ordenador)

        if puntos_jugador == 3:
            print("Felicidades, ganaste la partida")
            return 1
        if puntos_ordenador == 3:
            print("Perdiste la partida, vuelve a intentarlo")
            return 1

instrucciones()
menu()
puntuacion()
