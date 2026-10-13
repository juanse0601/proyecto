import sys
import os
import json

def tipo_encoding(ruta):
	try:
		with open(ruta,"r",encoding="utf-8") as f:
			return "utf-8"
	except UnicodeDecodeError:
		with open(ruta,"r",encoding="latin-1") as f:
			return "latin-1"
