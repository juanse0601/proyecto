import sys
import os
import json
from pathlib import Path

def tipo_encoding(ruta):
	try:
		with open(ruta,"r",encoding="utf-8") as f:
			f.read()
			return "utf-8"
	except UnicodeDecodeError:
		with open(ruta,"r",encoding="latin-1") as f:
			f.read()
			return "latin-1"

def cargar_json(diccionario:dict):
	base=Path.cwd()
	salida=Path("obs_json")
	salida.mkdir(exists_ok=True)
	rutasalida=base.joinpath(salida)
	with open(ruta, "w", encoding="utf-8") as archivo:
		##Revisar items que estan dentro json.dump(medicion, archivo, ensure_ascii=False, indent=2)
	
	


if __name__=='__main__':
	encoding=tipo_encoding(sys.argv[1])
	print(encoding)
