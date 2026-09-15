import sys

def estacompleto(dicc:dict) -> int:
	contador=0
	for ciudad,datos in dicc.items():
		if datos['Sensacion termica(C°)'] != 'No se calcula':
			contador=contador+1
	return contador		
