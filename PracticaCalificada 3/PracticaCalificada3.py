import  json
#P1
''' 
def generaBoleta():
    boleta ={}
    items = []
    producto = int(input("Ingrese el numero de productos: "))
    for i in range(producto):
        item = {}
        item["producto"] = input("Ingrese producto: ")
        item["precio"]= float(input("Ingrese precio: "))
        item["cantidad"] =int(input("Ingrese Cantidad :"))
        item["igv"] =round ((item["cantidad"]*item["precio"])*.18,2)
        item["total"] = (item["cantidad"]*item["precio"])+ item["igv"]
        items.append(item)
        boleta["items"] = items
    return boleta

def imprimirventa():
    total =0
    igv = 0
    for i in generaBoleta()["items"]:
        total+=i["total"]
        igv += i["igv"]
    print("El IGV es {} y monto a pagar es {} ". format(igv, round(total,2)))
imprimirventa()
'''
#P2
''' 
from random import randint
def crearmatriz(size):
    return [[ randint(1,9) if (i not in (0, size-1)) and (j not in (0, size-1)) else '*' for i in range(size)] for j in range(size)]

def imprimirmatriz(matriz, size):
    for i in range(size):
        for j in range(size):
            print(matriz[i][j], end=" ")
        print()

tamano =8
imprimirmatriz(crearmatriz(tamano),tamano)
'''
#p3
''' 
avion = [
    [0, 1, 1, 1],
    [1 ,1, 0, 1],
    [1, 1, 1 ,0],
    [1, 0, 1, 0],
    [1 ,0, 0 ,1],
    [0 ,1, 1, 1],
    [1 ,1, 0, 0],
    [1, 0, 0, 0],
    [1 ,1, 0 ,0],
    [1 ,1, 1, 0],
    [0, 0, 1, 0],
    [1, 1, 1, 0],
    [0 ,0, 1, 0],
    [-1 ,-1, -1, -1],
    [-1 ,-1 ,-1 ,-1],
    [1 ,0 ,1, 0],
    [1, 0, 0, 1],
    [0 ,1, 0, 1],
    [0 ,1 ,1, 0],
    [0 ,1 ,0 ,0]]
A,B,C,D = 0,0,0,0

for i in range(len(avion)):
    A += 1 if avion[i][0]==0 else 0
    B += 1 if avion[i][1]==0  else 0
    C += 1 if avion[i][2]==0  else 0
    D += 1 if avion[i][3]==0  else 0
print(A,20-A)
print(B,20-B)
print(C,20-C)
print(D,20-D)
'''
#P4
''' 
def cargar_datos():
    with open("elecciones2021.json","r", encoding='utf-8') as file:
        json_data = json.load(file)
        return json_data

def calcularvotos():
    mayor = 0
    nombre = ""
    i = 0
    for n in cargar_datos()["candidato"]:
        totalvotos = sum(n["votos"])
        if i ==0:
            mayor = totalvotos
        else:
            if totalvotos>mayor:
                mayor = totalvotos
                nombre = n["nombre"]
        i+=1
    return mayor,nombre

votos,candidato= calcularvotos()
print(candidato, votos)
'''