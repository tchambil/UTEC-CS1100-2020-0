from random import randint, choice
#P1
'''
letras = "abcdefghijklmnoprqstvwxyz"
def generarToken():
    token = ""
    # Escribe tu código aqui
    contarnumeros = 0
    while len(token) < 6:
        if token=="" or 6 ==len(token)+1:
            token += str(choice(letras)).upper()
        else:
            token += choice(letras)
        if contarnumeros < 2:
            token += str(randint(0, 9))
            contarnumeros += 1
    return token
print(generarToken())

#P2
def construilist(lista):
    newlista = []
    position = len(lista)-3
    print(position)
    lista.pop(1)
    lista.insert(1,lista[position])
    lista.pop(position+1)
    newlista = lista
    return newlista

#list= [14,15,25,35,14,48,86,48,14,16,80]
#llist =["Juan", "Luis", "Pedro","Maria","Carlos","Pedro","Manuel", "Miriam", "Jorge"]
list =["C","A","E","B","D","F","G","H","J","K","A"]
print(construilist(list))

#p3

def precio(servicio, distancia, tiempo):
    if servicio =="UBER":
        return 1.2*distancia+0.1*tiempo
    elif servicio =="Cabify":
        if distancia>20:
            return (((distancia-20)*1.1)+(20*1.65))
        else:
            return (distancia * 1.65)
    elif servicio =="TaxiBeat":
        return ((distancia*1.05)+(tiempo*0.34)+2.4)
    else:
        return 0

servicios =["UBER","Cabify","TaxiBeat"]
distancia = 200
tiempo = 160

for i in servicios:
    print(i, ":", round(precio(i,distancia,tiempo),2))
    
'''