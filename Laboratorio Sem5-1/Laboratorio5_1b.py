import  random

def generaMatriz(numfilas, numcols):
    matriz=[]
    for fila in range(numfilas):
        unafila = ["."]*numcols
        matriz.append(unafila)
    return matriz

def imprimirmatriz(matriz,numfilas, numcols):
    for fila in range(numfilas):
        for col in range(numcols):
            print(matriz[fila][col],end=" ")
        print()

def llenarmatriz(matriz, numfilas, numcols):
    colores = "ABCDEF"
    for fila in range(numfilas):
        for col in range(numcols):
            matriz[fila][col]= random.choice(colores)
    return matriz

def crearnuevamatriz(imagen, numfilas, numcols):
    colores =[]
    for i in range(0,numfilas-1):
        for j in range(0, numcols-1):
            if imagen[i][j]==imagen[i+1][j] and imagen[i][j]==imagen[i+1][j+1] and imagen[i][j]==imagen[i][j+1]:
                colores.append(imagen[i][j])

    nuevamatriz =[]
    for c in colores:
        for i in range(2):
            fila =[c]*2
            nuevamatriz.append(fila)
    imprimirmatriz(nuevamatriz,len(colores)*2,2 )

filas = 25
cols =25
mimatriz = generaMatriz(filas,cols)
mimatriz2= llenarmatriz(mimatriz, filas,cols)
imprimirmatriz(mimatriz2, filas,cols)
crearnuevamatriz(mimatriz2,filas,cols)



