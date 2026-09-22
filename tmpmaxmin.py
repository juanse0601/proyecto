import sys
from ciudades import nombre_ciudades
def topciudades(dicc:dict, tipodato:str, n:int, descendente:bool) ->list:
	lista=[(datos[tipodato],ciudad) for ciudad, datos in dicc.items()]
	if descendente==True:
		lista.sort(reverse=True)
	else:
		lista.sort(reverse=False)
	print(lista[:n])
	return 0

def tmpmax(dicc:dict) -> int:
	
	tmpmax=dicc['Azul']['temperatura(C)']
	for ciudad,datos in dicc.items():
		if datos['temperatura(C)'] > tmpmax:
			tmpmax=datos['temperatura(C)']	
	return tmpmax
	
def tmpmin(dicc:dict) -> int:	
	tmpmin=dicc['Azul']['temperatura(C)']
	for ciudad,datos in dicc.items():
		if datos['temperatura(C)'] < tmpmin:
			tmpmin=datos['temperatura(C)']	
	return tmpmin

def velmin(dicc:dict) -> int:	
	velmin=dicc['Azul']['temperatura(C)']
	for ciudad,datos in dicc.items():
		if datos['temperatura(C)'] < velmin:
			velmin=datos['temperatura(C)']	
	return velmin
			
def velmax(dicc:dict) -> int:	
	velmax=dicc['Azul']['temperatura(C)']
	for ciudad,datos in dicc.items():
		if datos['temperatura(C)'] > velmax:
			velmax=datos['temperatura(C)']	
	return velmax
	
			
