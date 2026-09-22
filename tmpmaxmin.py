import sys
from ciudades import nombre_ciudades
def topciudades(dicc:dict, tipodato:str, n:int, descendente:bool) ->list:
	lista=[(datos[tipodato],ciudad) for ciudad, datos in dicc.items()]
	if descendente==True:
		lista.sort(reverse=True)
	else:
		lista.sort(reverse=False)
	return lista[:n]

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
	velmin=dicc['Azul']['Velocidad_viento']
	for ciudad,datos in dicc.items():
		if datos['Velocidad_viento'] < velmin:
			velmin=datos['Velocidad_viento']	
	return velmin
			
def velmax(dicc:dict) -> int:	
	velmax=dicc['Azul']['Velocidad_viento']
	for ciudad,datos in dicc.items():
		if datos['Velocidad_viento'] > velmax:
			velmax=datos['Velocidad_viento']	
	return velmax
	
			
