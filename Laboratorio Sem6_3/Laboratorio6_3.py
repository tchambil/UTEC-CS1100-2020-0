'''numeros = [1,2,3,4,5,6,7,8]
r1= []
# lista clasicas
for e in numeros:
    e = e*2
    r1.append(e)
print(r1)

#Lista por comprensión
r2= [(e*2) for e in numeros]
print(r2)

strings = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
r3=[]
# lista clasicas
for e in strings:
    e = e.upper()
    r3.append(e)
print(r3)
#Lista por comprensión
r4= [ e.upper() for e in strings]
print(r4)

A = [x for x in range(2,25,2)]
B=  [x for x in range(3,28,3)]
print(A)
print(B)


import random

C = [random.randint(0,9) for x in range(100)]

print(C)

Escribir un programa que genere la lista de números entre 0 y 50
que no sean pares y que no sean múltiplos de 3


lista = [x for x in range(0,50) if x % 2!=0 and x %3 !=0]
print(lista)


texto = "10, 20, 33, 40, 11, 90"
lista = [int(x) for x in texto.split(',')]
#suma = sum([int(x) for x in texto.split(',') if int(x)%10==0]) usando texto
suma = sum([x for x in lista if x%10==0])
print(suma)

#Dados el conjunto C, definir una lista que sea la suma de las filas y
#calcular el total de todos los valores

C= [[2,3,4],
    [40,50,60],
    [100,200,300]]

sum_row1 = [sum(x) for x in C]
print(sum_row1)
# equivalente usando for
sum_row2 = []
for row in C:
    subtotal = sum(row)
    sum_row2.append(subtotal)
print(sum_row2)

#suma total
total1= sum([x for row in C for x in row])
print(total1)
#equivalnete usando for
total2=0
for row in C:
    for x in row:
        total2 +=x
print(total2)

'''
''' Crear una matriz de identidad
[1, 0, 0, 0, 0]
[0, 1, 0, 0, 0]
[0, 0, 1, 0, 0]
[0, 0, 0, 1, 0]
[0, 0, 0, 0, 1]
'''
'''
def crearmatrix(n):
    matriz = []
    for fila in range(n):
        elemento = []
        for col in range(n):
            if fila == col:
                elemento.append(1)
            else:
                elemento.append(0)
        matriz.append(elemento)
    return matriz

def crearmatriz_identidad(n):
    return [[(1 if col == fila else 0) for col in range(n)] for fila in range(n)]

for i in crearmatriz_identidad(5):
    print(i)
'''

'''
supongamos que tengo cuatro camisas (de color rojo, amarillo, azul y verde)
y dos pantalones (de color negro y blanco). Quiero saber de qué manera
puedo combinar mi ropa. Hay ocho formas distintas (4 camisas × 2 pantalones)
de hacerlo:
Camisa roja y pantalón negro.
Camisa roja y pantalón blanco.
Camisa amarilla y pantalón negro.
Camisa amarilla y pantalón blanco.
Camisa azul y pantalón negro.
Camisa azul y pantalón blanco.
Camisa verde y pantalón negro.
Camisa verde y pantalón blanco.
output:
[('rojo', 'negro'), ('rojo', 'blanco'),
 ('amarillo', 'negro'), ('amarillo', 'blanco'),
 ('azul', 'negro'), ('azul', 'blanco'),
 ('verde', 'negro'), ('verde', 'blanco')] 

pantalones = ['pantalon negro','pantalon blanco']
camisas = ['camisa rojo','camisa  amarillo','camisa azul','camisa verde']
ropa = [(c, p) for c in  pantalones for p in  camisas]
for i in ropa:
    print(i)
'''






