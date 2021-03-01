import random
filas= 20
columnas =10
tablero =[]
pokemones = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
vidas =[3 for _ in range(len(pokemones))]
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

def colisiones(pokemon):
    index = pokemones.find(pokemon)
    vidas[index]-=1

def imprimircolisiones():
    for i in range(len(pokemones)):
        if vidas[i]<3:
            print("Al pokemon {} le queda {} vidas".format(pokemones[i], vidas[i]))

def aleatoriopokemon(cant):

    if len(pokemones) <cant:
        print("La cantidad de pokemos a generar es insuficiente")
        return True
    i =0
    while i<cant:
        elegido = random.choice(pokemones)

        if not validarepetido(elegido):
            pfila = aletorio(0, filas - 1)
            pcolumna =aletorio(0, columnas - 1)

            if tablero[pfila][pcolumna] ==".":
                tablero[pfila][pcolumna] = elegido
                i+=1
            else:
                npokemon = tablero[pfila][pcolumna]
                colisiones(npokemon)
                colisiones(elegido)
                print("Los pokemones {} {} colisionaron ".format(npokemon, elegido) )

generarTablero()
if not aleatoriopokemon(25):
    imprimirTablero()
    imprimircolisiones()