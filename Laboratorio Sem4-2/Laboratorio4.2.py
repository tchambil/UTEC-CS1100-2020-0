'''El profesor del curso de ICC quiere ayudar aquellos alumnos
que les fue mal en el último PC. Para ello, el profesor subirá más
ejercicios  para que los alumnos aumenten su puntaje. En este escenario,
 la nota mínima aprobatoria sería el promedio de todos los alumnos que
  si aprobaron. Ayude a identificar aquellos alumnos que tienen una nota menor a 10.5
e indique cuantos puntos como mínimo necesita cada uno para superar
 la nota promedio previamente calculado.

Input:
Juana,16.5
Luis,10
Carmen,17
Sara,08
Joel,10.5
Matias,15

output:
Luis,4.75
Sara,6.75
 '''

import random

def aletorio(min, max):
    n = random.randint(min, max)
    return n

def generarlista(n):
    lista =[]
    for i in range(n):
        lista.append(aletorio(5,500))
    return  lista

def imprimirlista(lista):
    for i in lista:
        print(i, end=" ")
    print()

#retorna 2 lista con numeros pares e impares
def generarparesimpares(lista):
    pares=[]
    impares=[]
    for i in lista:
        if i%2==0:
            pares.append(i)
        else:
            impares.append(i)
    return pares,impares

'''
resultado = generarlista(20)

_pares, _impares= generarparesimpares(resultado)
imprimirlista(resultado)
imprimirlista(_pares)
imprimirlista(_impares)

filas =4
columnas =6
matriz=[]
for i in range(filas):
    fila = [0]*columnas
    matriz.append(fila)

for i in matriz:
    print(i)
print()

for f in range(filas):
    for c in range(columnas):
        matriz[f][c]=aletorio(5,50)
for i in matriz:
    print(i)
'''
#nombre, apellido, edad, talla, peso, genero
alumnos = [ ["Luis", "Yi",                19, 1.82, 80, "M"],
      ["Paul", "Tipula",           19, 1.90, 72,"M"],
      ["Joaquin", "Cayo",       22, 1.80, 90,"M"],
      ["Martin", "Robles",       17, 1.60, 62,"M"],
      ["Luis", "Piñas",             21, 1.80, 70,"M"],
      ["Diana", "Garcia",        16, 1.60, 60,"F"],
      ["Paul", "Tipula",           19, 1.70, 72,"M"],
      ["Manuel", "Gonzalez", 16, 1.70, 73,"M"],
      ["Carlos", "Segura",      19, 1.73, 68,"M"],
      ["Giordano", "Alvites",   23, 1.83, 82,"M"],
      ["Alfieri", "Podesta",      17, 1.77, 60,"M"],
      ["Ana", "Adriano",         18, 1.63, 57,"F"]
    ]

def promedioEdad(alumnos):
    suma = 0
    prom = 0
    for i in range(len(alumnos)):
        suma+=alumnos[i][2]
    prom = suma/len(alumnos)
    return round(prom,2)

#El nombre del alumno mas joven
def alumnoJoven(alumnos):
    pass
#el nombre del alumno tiene menor peso
def alumnoPeso(alumno):
    pass
# lista de hombres y mujeres
def dividirlista(alumno):
    pass

print(promedioEdad(alumnos))


#for i in range(len(alumnos)):
#    print(alumnos[i][0],alumnos[i][1],alumnos[i][2],alumnos[i][3])

#imprimirlista(alumnos)

frase ="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum".lower()
alfabeto =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z']
contador = [0 for _ in range(27)]

print(contador)
for letra in frase:
    i=0
    for car in alfabeto:
        if letra == car:
            contador[i]+=1
        i+=1
i=0
while i<27:
    if contador[i]>0:
        print(alfabeto[i],": ", contador[i])
    i+=1





































