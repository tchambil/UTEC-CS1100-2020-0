'''
Interface Status
ref: https://github.com/chrhobbs/exercise-python-json-parsing 
================================================================================
DN                                                 Description           Speed    MTU
-------------------------------------------------- --------------------  ------  ------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150
topology/pod-1/node-201/sys/phys-[eth1/35]
'''
'''
import  json

jsondata = open('exer1-interface-data.json').read()
json_object = json.loads(jsondata)
print(
    "=======================================================================================" "\n"
    "DN                                                 Description           Speed    MTU" "\n" 
    "-------------------------------------------------- --------------------  ------  ------")
imdata =json_object["imdata"]
for i in imdata:
    dn=i["l1PhysIf"]["attributes"]["dn"]
    descr = i["l1PhysIf"]["attributes"]["descr"]
    speed= i["l1PhysIf"]["attributes"]["speed"]
    mtu = i["l1PhysIf"]["attributes"]["mtu"]
    print("{} {} {} {}".format(dn,descr,speed,mtu))
 #Descargando archivos JSON desde la Web
import json
import urllib.request
leendo = urllib.request.urlopen("http://fspreset.minagri.gob.pe:5000/datos_abiertos_ne")
abierto = leendo.read()
jsons = json.loads(abierto)

for i in range(len(jsons)):
    for key, value in jsons[i].items():
        print(key,": ", value)
    print()
   '''
#Leendo archivo csv
import csv
with open('Diccionario_Datos.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ';',  skipinitialspace=True)
    for row in reader:
        print(row)





