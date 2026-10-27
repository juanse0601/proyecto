import sys
import datetime
import funciones
import os
import json
from pathlib import Path
import funciones_smn

if len(sys.argv)==2:
	try:
		extension=sys.argv[1].split('.')[-1]
		#Lee el .json si existe
		if extension=='json':
			funciones_smn.leer_json(sys.argv[1])
		#Carga el diccionario y lo guarda en .json y por ultimo lo lee
		elif extension=='txt':
			diccionario=funciones.leer_observaciones(sys.argv[1])
			funciones_smn.cargar_json(diccionario,sys.argv[1])
			funciones_smn.leer_json(sys.argv[1])
		else:
			print("No se encontro una extension valida")
	except FileNotFoundError:
		print("El archivo no existe")
elif len(sys.argv)>2: #Mas de 2 parametros
		print("Hay parametros de mas")
else: #Menos de 2 parametros
		funciones_smn.buscar_archivos()
		
		

