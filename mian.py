import random

PIEDRA = 0
PAPEL = 1
TIJERA = 2

def instrucciones():
    print("Vas a jugar a piedra, papel, tijeras.")
    print("Gana el primero en llegar a 3 puntos, tu contrincante es el ordenador. Buena suerte!")


def menu():
    print("0 -> Piedra")
    print("1 -> Papel")
    print("2 -> Tijeras")


def escoger_rondas():
    rondas = 0
    while rondas != 3 and rondas != 5 and rondas != 10:
        rondas = int(input("¿Cuántas rondas quires jugar? Escoge entre 3, 5 o 10 rondas."))
        if rondas == 3 or rondas == 5 or rondas == 10: #Verifica si el usuario introduce 3,5 o 10
            print("Has seleccionado:", rondas, "rondas.")
            return rondas
        else:
            print ("Selecciona un valor válido.")


def escoger_dificultad():
    dificultad = ""
    while dificultad != "facil" and dificultad != "normal" and dificultad != "dificil":
        dificultad = input("Escoge la dificultad que quieras. Facil/Normal/Dificil").lower()
        if dificultad == "facil" or dificultad == "normal" or dificultad == "dificil":
            print("Selecciona una opcion válida")
    return dificultad


def eleccion_jugador():
    jugador = -1

    while jugador <= -1:
        jugador = int(input("Escoge tu elección"))
        if jugador == PIEDRA:
            print("Piedra")
        elif jugador == PAPEL:
            print("Papel")
        elif jugador == TIJERA:
            print("Tijeras")
        else:
            print("Escoge un valor correcto")
    return jugador


def eleccion_ordenador(dificultad, eleccion_jugador):
    if dificultad == "facil":
        if random.randint(0,1) == 0: 
            return PIEDRA # 50% de elegir piedra
        else:
            return random.randint(PIEDRA,TIJERA) # 50% de elegir aleatoriamente
    elif dificultad == "dificil":
        if random.randint(1,10) <= 2: # 20% de elegir aleatoriamente
            return random.randint(PIEDRA, TIJERA)
        else: # 20% de elegir la opcion ganadora 
            return (eleccion_jugador + 1) % 3 
    else: #dificultad normal
        return random.randint(0,2) # Escoge aleatoriamente
    
    
def puntuacion (rondas, dificultad):
    puntos_jugador = 0
    puntos_ordenador = 0

    while puntos_jugador <= 3 or puntos_ordenador <= 3:

        jugador = eleccion_jugador()
        ordenador = eleccion_ordenador(dificultad, jugador)

        if jugador == ordenador:
            print("Empate")
        elif (jugador == PIEDRA and ordenador == TIJERA) | (jugador == PAPEL and ordenador == PIEDRA) | (jugador == TIJERA and ordenador == PAPEL):
            puntos_jugador += 1 #Se suma en 1 el valor de los puntos del jugador 
            print("Ganaste la ronda")
        else:
            puntos_ordenador += 1 #Se suma en 1 el valor de los puntos del ordenador
            print("Perdiste la ronda")
        
        print("Tus puntos:", puntos_jugador, "Puntos ordenador:", puntos_ordenador)

        if puntos_jugador == rondas: #se termina cuando los puntos de jugador sean igual a las rondas seleccionadas
            print("Felicidades, ganaste la partida")
        if puntos_ordenador == rondas: #se termina cuando los puntos del ordenador sean igual a las rondas seleccionadas
            print("Perdiste la partida, vuelve a intentarlo")
        


#Inicia el juego
instrucciones()
rondas = escoger_rondas()
dificultad = escoger_dificultad()
menu()
puntuacion(rondas, dificultad)


