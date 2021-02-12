class Solution:
    '''
    P1) Una de las políticas de la UTEC es premiar a los mejores estudiantes con BECAS para
    pasantías en Universidades Extranjeras y Alejandro es candidato para una
    pasantía en “Harvard University”. Él se averiguó las notas, de las Practicas Calificadas (PCs)
    del curso CS1100,de los 4 candidatos y quiere saber quien tiene el promedio más alto, las notas son lo siguiente:
            PC1   PC2  PC3  PC4
        1)  10     16     13     16
        2)  17     14     11     15
        3)  12     17     16     17
        4)  15     16     16     15

    P2) En el curso “Introducción a la Ciencia de la Computación” el profesor desea eximir del
     “Examen Final” a los alumnos que tienen promedio mayor a 15, pero, siempre y cuando no haya
     desaprobado ninguna PC.  Se sabe que el alumno dio tres PC’s. Escriba un algoritmo que permita
      imprimir los alumnos eximidos con su respectivo promedio,
      las notas son como sigue:
              PC1   PC2  PC3
        1)  10     16     13
        2)  17     10     11
        3)  15     17     14
        4)  10     16     16
        5)  10     16     16
        6)  10     16     16
        7)  10     16     16
    '''
    def Pregunta1(self):
        mayor =0
        for i in range(4):
            sumanota = 0
            for j in range(4):
                nota = int(input("Ingrese la nota [{}] del alumno [{}]: ".format(j+1,i+1)))
                sumanota +=nota
            promedio = sumanota/j
            print("El promedio del alumno[{}] es: {:.2f}".format(i+1,promedio))
            if i==0:
                mayor= promedio
            if promedio> mayor:
                mayor = promedio
        print("El promedio mas alto es: ",mayor)

    def Pregunta2(self):
         pass


Solution().Pregunta1()
Solution().Pregunta2()
