from flask import Flask, render_template, request
import json
app = Flask(__name__)
def cargar_datos():
    with open("elecciones2021.json","r",encoding='utf-8') as file:
        json_data = json.load(file)
        return json_data

def selectionSort(lista):
    for i in range(len(lista)):
        min = i
        for j in range(i+1, len(lista)):
            if lista[j]['nombre'] < lista[min]['nombre']:
                min = j
        lista[i], lista[min] = lista[min], lista[i]
    return lista

def busquedabinaria(lista, nombre):
    min=0
    max =len(lista)-1
    while True:
        if max < min: return None
        mid = (min + max) // 2
        if lista[mid]['nombre'] < nombre: min = mid+1
        elif lista[mid]['nombre'] > nombre: max = mid-1
        else: return lista[mid]

@app.route('/', methods=['POST', 'GET'])
def index():
    mostrar = []
    resultado = cargar_datos()['candidato']
    if request.method == 'POST':
        nombredelcandidato = request.form['nombre']
        try:
            result = (busquedabinaria(selectionSort(resultado), nombredelcandidato))
            if result==None:
                mostrar = []
            else:
                mostrar.append(result)
            return render_template('index.html', candidatos=mostrar)
        except:
            return 'Ocurrío un problema al buscar'
    else:
        return render_template('index.html', candidatos=resultado)


