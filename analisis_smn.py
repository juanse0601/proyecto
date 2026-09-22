import sys
import datetime
from cargardicc import cargar
from ciudades import nombre_ciudades
from ciudadescompletas import estacompleto
import tmpmaxmin
diccionario=cargar(sys.argv[1])
largodicc=len(diccionario)
lista=['ciudad/estacion','fecha','hora','condicion del cielo','visibilidad','temperatura(C)','Sensacion termica(C)','Humedad','Direccion_viento','Velocidad_viento','Presion']

print('Pruebas')
print(' 5 ciudades con mayor velocidad de viento:',tmpmaxmin.topciudades(diccionario,'Velocidad_viento',5,True))
print(' 7 ciudades con menor temperatura:',tmpmaxmin.topciudades(diccionario,'temperatura(C)',7,False))
print('Velocidad max:',tmpmaxmin.velmax(diccionario))
print('Velocidad min:',tmpmaxmin.velmin(diccionario))
print('Temperatura max:',tmpmaxmin.tmpmax(diccionario))
print('Temperatura min:',tmpmaxmin.tmpmin(diccionario))
