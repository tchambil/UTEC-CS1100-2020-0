from random import randint, choice
#Jugando con conceptos de STRING
#Generemos un token digital o codigos captch básicos
token =""
letras = "abcdefghijklmnoprqstvwxyz"
#queremos lograr que tenga dos números y el restro letras
#  (no importa posición)
contarnumeros = 0
while len(token) <6:
    token +=choice(letras)
    if contarnumeros<2:
        token += str(randint(0, 9))
        contarnumeros+=1
print(token)



