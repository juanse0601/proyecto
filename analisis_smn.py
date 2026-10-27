import sys
import datetime
import funciones
import os
import json
from pathlib import Path
import funciones_smn
#lista=['ciudad/estacion','fecha','hora','condicion del cielo','visibilidad','temperatura(C)','Sensacion termica(C)','Humedad','Direccion_viento','Velocidad_viento','Presion']

diccionario={}
try:
	if len(sys.argv)==2:
		extension=sys.argv[1].split('.')[-1]
		if extension=='txt':
			diccionario=funciones.leer_observaciones(sys.argv[1])
			funciones.leerdatos(diccionario)
		else:
			print("Extension de archivo no valido")
			
	elif len(sys.argv)>2: #Mas de 2 parametros
		print("Hay parametros de mas")
	else: #Menos de 2 parametros
		print("Faltan parametros")
except FileNotFoundError:
	print("El archivo no existe")	
	
