import random
 # Seguir en funcion puntuacion haciendo racha ordenador
PIEDRA = 0
PAPEL = 1
TIJERA = 2

FACIL = "facil"
NORMAL = "normal"
DIFICIL = "dificil"

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
        if rondas == 3 or rondas == 5 or rondas == 10: # Verifica si el usuario introduce 3,5 o 10
            print("Has seleccionado:", rondas, "rondas.")
            return rondas
        else:
            print ("Selecciona un valor válido.")


def escoger_dificultad():
    dificultad = ""
    while dificultad != FACIL and dificultad != NORMAL and dificultad != DIFICIL:
        dificultad = input("Escoge la dificultad que quieras. Facil/Normal/Dificil").lower()
        if dificultad != FACIL or dificultad != NORMAL or dificultad != DIFICIL:
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
    else: # Dificultad normal
        return random.randint(0,2) # Escoge aleatoriamente
    
    
def puntuacion (rondas, dificultad):
    puntos_jugador = 0
    puntos_ordenador = 0
    racha_jugador = 0
    racha_ordenador = 0

    while puntos_jugador < rondas and puntos_ordenador < rondas:

        jugador = eleccion_jugador()
        ordenador = eleccion_ordenador(dificultad, jugador)

        if jugador == ordenador:
            print("Empate")
            racha_jugador = 0
            racha_ordenador = 0
        elif (jugador == PIEDRA and ordenador == TIJERA) or (jugador == PAPEL and ordenador == PIEDRA) or (jugador == TIJERA and ordenador == PAPEL):
            puntos_jugador += 1 # Se suma en 1 el valor de los puntos del jugador 
            racha_jugador += 1  # Se suma en 1 el valor de la racha de victorias del jugador 
            racha_ordenador = 0
            print("Ganaste la ronda")
        else:
            puntos_ordenador += 1 # Se suma en 1 el valor de los puntos del ordenador
            racha_ordenador += 1 # Se suma en 1 el valor de la racha de victorias del ordenador
            racha_jugador = 0
            print("Perdiste la ronda")
        
        if racha_jugador == 3 and (dificultad == FACIL or dificultad == NORMAL):
            puntos_jugador += 1
            print("Has conseguido una racha de 3, ganas un pun to extra.")
            racha_jugador = 0 # Se reinicia la racha

        if racha_ordenador == 3: ###################################################################

            print("Tus puntos:", puntos_jugador, "Puntos ordenador:", puntos_ordenador)

        if puntos_jugador == rondas: # Se termina cuando los puntos de jugador sean igual a las rondas seleccionadas
            print("Felicidades, ganaste la partida")
        if puntos_ordenador == rondas: # Se termina cuando los puntos del ordenador sean igual a las rondas seleccionadas
            print("Perdiste la partida, vuelve a intentarlo")
        


#Inicia el juego
instrucciones()
rondas = escoger_rondas()
dificultad = escoger_dificultad()
menu()
puntuacion(rondas, dificultad)


