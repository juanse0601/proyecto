import sys
import os
import json
from pathlib import Path
import datetime


def tipo_encoding(ruta):
	try:
		with open(ruta,"r",encoding="utf-8") as f:
			f.read()
			return "utf-8"
	except UnicodeDecodeError:
		with open(ruta,"r",encoding="latin-1") as f:
			f.read()
			return "latin-1"

def cargar_json(diccionario:dict,nombresalida:str):
	diccionario=convertir_fecha(diccionario)
	base=Path.cwd()
	salida=Path("obs_json")
	if salida.exists():
		print("La carpeta obs_json ya existe")
	else:
		print("Creando la carpeta obs_json")
		salida.mkdir(exist_ok=True)
	salida_sin_txt=Path(nombresalida).stem #Elimina extension .txt
	rutasalida=base/salida/f"{salida_sin_txt}.json"
	with open(rutasalida,"w", encoding="utf-8") as archivo:
		json.dump(diccionario, archivo, ensure_ascii=False, indent=2)

def leer_json(ruta):
	base=Path.cwd()
	salida=Path("obs_json")
	if salida.exists():
		
	else:
		print("No existe la carpeta obs_json")
	
	
def convertir_fecha(dicc:dict):
	for ciudad,elemento in dicc.items():
		dicc[ciudad]["fecha y hora"]=dicc[ciudad]["fecha y hora"].isoformat(timespec='minutes')	
	return dicc


if __name__=='__main__':
	encoding=tipo_encoding(sys.argv[1])
	print(encoding)
