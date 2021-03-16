'''La empresa “Factorías del Perú”, recientemente adquirió un nuevo sensor de temperatura para
medir la temperatura del centro de incubadora y se requiere obtener las dos(2) temperaturas
más altas con la indicación de la hora, min, seg en el que ocurrió dicho evento. Se debe
almacenar el resultado del sensor en un archivo y luego ordenarla y obtener cual
fue el mayor en que hora, min, segundo. (si hay empates mostrarlos)'''
import  time
import  random
def sensorTemp():
    seg = 0
    min = 0
    hora = 0
    f = open("C:/Users/User/PycharmProjects/CursoICC/venv/texto.dat", "a")
    while seg<=120:
        valor = "Tiempo: {} : {} : {} => °C {}".format(hora,min,seg, random.randrange(0,101,2))
        f.write(valor+"\n")
        print(valor)
        seg += 1
        if seg ==60:
            seg=0
            min+=1
            hora =int(min/60)
        time.sleep(1)
    f.close()
sensorTemp()


