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

eleccion_jugador()



