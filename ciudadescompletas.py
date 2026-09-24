import sys

def estacompleto(dicc:dict) -> int:
	contador=0
	for ciudad,datos in dicc.items():
		if datos['Sensacion termica(C)'] != 'No se calcula':
			contador=contador+1
	return contador		

def listaciudadescompletas(dicc:dict) -> int:
	lista=[]
	for ciudad,datos in dicc.items():
		if datos['Sensacion termica(C)'] != 'No se calcula':
			lista.append(ciudad)
	return lista
