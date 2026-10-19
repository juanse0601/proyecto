import sys
import os
import json
from pathlib import Path
import datetime

def tipo_encoding(ruta):
	##Probamos si puede leer utf-8
	try:
		with open(ruta,"r",encoding="utf-8") as f:
			f.read()
			return "utf-8"
	##Si no lee utf-8 probamos que lea latin-1
	except UnicodeDecodeError:
		with open(ruta,"r",encoding="latin-1") as f:
			f.read()
			return "latin-1"

def cargar_json(diccionario:dict,nombresalida:str):
	##cambiamos la fecha
	diccionario=convertir_fecha(diccionario)
	##Creamos la ruta
	base=Path.cwd()
	salida=Path("obs_json")
	##Verificamos si existe la ruta
	if salida.exists():
		print("La carpeta obs_json ya existe")
	else:
		print("Creando la carpeta obs_json")
		salida.mkdir(exist_ok=True)	
	
	salida_sin_txt=Path(nombresalida).stem #Elimina extension .txt
	rutasalida=base/salida/f"{salida_sin_txt}.json" ##terminamos de crear la ruta
	##Cargamos el json
	with open(rutasalida,"w", encoding="utf-8") as archivo:
		json.dump(diccionario, archivo, ensure_ascii=False, indent=2)

def leer_json(nombresalida:str):
	base=Path.cwd()
	salida=Path("obs_json")
	salida_sin_txt=Path(nombresalida).stem #Elimina extension .txt
	rutasalida=base/salida/f"{salida_sin_txt}.json" ##terminamos de crear la ruta
	
	try:
		with open(rutasalida,"r",encoding='utf-8') as f:
			datos=json.load(f)
		ciudades=len(datos)
		print(f"Hay {ciudades} ciudades")
		informadas=0
		for nombre in datos.values():
			if nombre: #True si la clave tiene un valor no nulo("",None,{},[],())
				informadas=informadas+1
		print(f"Hay {informadas} ciudades informadas")
	except FileNotFoundError:
		print(f"La ruta {rutasalida} no existe")

def buscar_archivos():
	print("Faltan parametros")
	try:
		rutatxt = os.listdir("datos")
		cantidadtxt = [nombre for nombre in rutatxt if nombre.endswith(".txt")]
		print(f"Hay {len(cantidadtxt)} archivos txt:",cantidadtxt)
		rutajson = os.listdir("obs_json")
		cantidadjson = [nombre for nombre in rutajson if nombre.endswith(".json")]
		print(f"Hay {len(cantidadjson)} archivos json:",cantidadjson)
	except FileNotFoundError:
		print("No existe la ruta")
	
	
		
			
def convertir_fecha(dicc:dict):
	##Convertimos las fechas dentro del diccionario usando .isoformat(timespec='minutes')
	for ciudad,elemento in dicc.items():
		dicc[ciudad]["fecha y hora"]=dicc[ciudad]["fecha y hora"].isoformat(timespec='minutes')	
	return dicc
	



if __name__=='__main__':
	diccionario=cargar(sys.argv[1])
