from Laboratorio3_3 import *
from time import sleep
#Jugando con conceptos de funciones y decoradores
#----------Ejemplo base------
def revisar(func):
    def otra_funcion(a,b):
        if b==0:
            print("No se puede dividir entre 0")
        return func(a,b)
    return otra_funcion

@revisar
def division(a,b):
    return a/b
#----------Fin de base------
def verificaCelular(func):
    #Solo para un argumento
    def validar(numero):
        if obtenerestadogeneral():
            print("El equipo esta preparado")
            func(numero)
        else:
           print("El equipo esta "+ "apagado " * (not obtenerestado()) +" bloqueado"* (not obtenerestadobloqueado()))
    return validar

def verificaEquipo(func):
    #Solo para N argumento
    def validar(*args, **kwargs):
        if obtenerestadogeneral():
            print("El equipo esta preparado")
            func(*args, **kwargs)
        else:
           print("El equipo esta "+ "apagado " * (not obtenerestado()) +" bloqueado"* (not obtenerestadobloqueado()))
    return validar

@verificaCelular
def llamarnuevo(numero):
    print("Llamando a {}".format(numero))

def autenticar(func):
    def validar(*args, **kwargs):
        if obtenerestadobloqueado()==False:
            patron = input("El equipo esta bloqueado, ingrese patron: ")
            if(patron=="1234"):
                func(*args, **kwargs)
            else:
                print("Patron Incorrecto ")
        else:
            func(*args, **kwargs)
    return validar

@autenticar
def descargaApp(nombre):
    print("Descargando... ", nombre)

def tiempo_espera(config={}):
    #'decorador que hace esperar la ejecucion de una funcion'
    def espera(func):
        def configuracion(*tup, **dic):
            print('debes esperar {time_to_wait} sec para llamar {name}'.format(**config))
            sleep(config['time_to_wait'])
            func(*tup, **dic)
        return configuracion
    return espera

@tiempo_espera({'time_to_wait': 5, 'name': 'apagar_equipo'})
def apagarequipo():
    print("Apagando el equipo")

def cargarbateria(valor):
    # debe ir acumulando la carga maximo debe 100 ( si llego a 100 imprime baterial completa)
    pass

encender()
desbloquear("1234d")
print("Estado",obtenerestado())
print("Desbloqueado",obtenerestadobloqueado())
llamarnuevo("9999")
descargaApp("Facebook")
apagarequipo()