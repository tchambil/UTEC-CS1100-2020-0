'''
P1)  Diseñe un algoritmo que simule la autenticación de un cajero automático
y que al tercer intento bloquee la cuenta por 10seg e imprima
 los segundos  que queda para volver a intentar y cuando la
  autenticación sea exitosa imprima:
 ******************************
  [1] Depositar
  [2] Retirar
  [3] Salir
******************************
'''
import time
intento=0
contrasenaCorrecta = "123456"

while True:
    contresena= input("Ingrese su contraseña: ")
    if contresena == contrasenaCorrecta:
        print("Puede realizar las siguiente Operaciones")
        print("-"*30)
        print("[1] Depositar")
        print("[2] Retirar")
        print("[3] Salir")
        print("-" * 30)
        opciones = input("Eliga una opción: ")
        #se puede hacer mas cosas . . . . . .
        break
    else:
        intento+=1
        print("Contraseña incorrecta, intento N°{}".format(intento))
        if intento==3:
            print("Llegaste al los 3 intentos, tu cuenta se encuentra bloqueda")
            segundos =10
            while True:
                print("Intenta en {} Seg.".format(segundos))
                segundos-=1
                time.sleep(1)
                if segundos==0:
                    intento=0
                    break
        else:
            continue


'''
P2) Se nos viene la próxima elección presidencial que se realizará en Perú este 21 de abril 
del 2021 y cuando se trata de votaciones electrónicas, la integridad de los datos es crucial. 
En esta oportunidad solo se presentaron dos candidatos al cual denominaremos Candidato1 
(Juan Perez) y Candidato2 (Jorge Perez). Siendo además los electores una cantidad de N. 
Se desea elaborar un algoritmo para contabilizar los votos, donde el elector puede:
 elegir un candidato o votar en blanco o viciar su voto, como resultado final se requiere 
 saber quien fue el candidato ganador, cantidad de votos blancos, viciados y el total de votos. 

'''