import random
filas= 40
columnas =20
tablero =[]
def aletorio(min, max):
    n = random.randint(min, max)
    return n

def generarTablero():
    for i in range(filas):
        fila =["."] * columnas
        tablero.append(fila)

def imprimirTablero():
    for i in range(filas):
        for j in range(columnas):
            print(tablero[i][j], end=" ")
        print()

def validarepetido(pokemon): # True o False (True si exite ya el pokemon y false si no existe)
    result = False
    for i in range(filas):
        for j in range(columnas):
            if tablero[i][j]==pokemon:
                return True
            else:
                result= False
    return  result


def aleatoriopokemon(cant):
    pokemones = "ABCDEFGHIJ"
    vidas =[3 for _ in range(len(pokemones))]
    if len(pokemones) <cant:
        print("La cantidad de pokemos a generar es insuficiente")
        return True
    #for i in range(cant):
    #    tablero[aletorio(0,filas-1)][aletorio(0,columnas-1)] =random.choice(pokemones)
    i =0
    while i<cant:
        elegido = random.choice(pokemones)
        if not validarepetido(elegido):
            tablero[aletorio(0, filas - 1)][aletorio(0, columnas - 1)] = elegido
            i+=1

generarTablero()
if not aleatoriopokemon(10):
    imprimirTablero()