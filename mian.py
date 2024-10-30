print("Vas a jugar a piedra, papel, tijeras.")

def menu():
    print("0 -> Piedra")
    print("1 -> Papel")
    print("2 -> Tijeras")

menu()

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

jugador = eleccion_jugador()

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


ordenador  = eleccion_ordenador()


def resultado (eleccion_jugador, eleccion_ordenador):

    if eleccion_jugador == eleccion_ordenador:
        print("Empate")
        return 0 #Empate
    elif (eleccion_jugador == 0 and eleccion_ordenador == 2) or (eleccion_jugador == 1 and eleccion_ordenador == 0) or (eleccion_jugador == 2 and eleccion_ordenador == 1):
        print("Ganaste la ronda")
        return 1 #Gana el usuario
    else:
        print("Perdiste la ronda")
        return -1 #Gana el ordenador
