import time
#Jugando con conceptos de funciones
#Implementando funciones básicas de un celular.
estado =False
Desbloqueado= False
def encender():
    global estado
    estado =True

def apagar():
    global estado
    estado=False

def obtenerestado():
    return  estado

def obtenerestadogeneral():
    return estado and Desbloqueado

def desbloquear(patron):
    clave="1234"
    global Desbloqueado
    if obtenerestado():
        if patron==clave:
            Desbloqueado = True
        else:
            Desbloqueado = False
    else:
        print("El equipo se encuentra apagado")


def HoraActual():
    hora_local = time.localtime()
    result = time.strftime("%I:%M:%S %p", hora_local)
    print(result)

def llamar(numero):
    if obtenerestadogeneral():
        print("Llamando a {}".format(numero))
    else:
        print("El equipo esta apagado" * (not estado))
        print("El equipo esta bloqueado" * (not Desbloqueado))

def agregarContacto(nombre):
    #agregando nuevo contactos
    pass

def imprimircontactos():
    #debe imprimir los contactos
    pass

def cargarbateria(valor):
    # debe ir acumulando la carga maximo debe 100 ( si llego a 100 imprime baterial completa)
    pass

def obtenerbateria():
    #devolver cual es la carga de la bateria
    pass



HoraActual()
print("Estado",estado)
print("Desbloqueado",Desbloqueado)
encender()
print("Estado",estado)
desbloquear("1234")
print("Desbloqueado",Desbloqueado)
llamar("123456789")
print("Estado General",obtenerestadogeneral())
