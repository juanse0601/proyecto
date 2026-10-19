import sys
import datetime
import funciones
import os
import json
from pathlib import Path
import funcionesjson
#lista=['ciudad/estacion','fecha','hora','condicion del cielo','visibilidad','temperatura(C)','Sensacion termica(C)','Humedad','Direccion_viento','Velocidad_viento','Presion']


if len(sys.argv)==2:
	extension=sys.argv[1].split('.')[-1]
	#Lee el .json si existe
	if extension=='json':
		funcionesjson.leer_json(sys.argv[1])
	#Carga el diccionario y lo guarda en .json y por ultimo lo lee
	elif extension=='txt':
		diccionario=funciones.cargar(sys.argv[1])
		funcionesjson.cargar_json(diccionario,sys.argv[1])
		funcionesjson.leer_json(sys.argv[1])
	else:
		print("No se encontró una extension valida")
		
		
		
elif len(sys.argv)>2: #Mas de 2 parametros
	print("Hay parametros de mas")
else: #Menos de 2 parametros
	funcionesjson.buscar_archivos()
	
	
