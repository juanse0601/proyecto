import sys
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
				
def ciudades(dicc:dict,tipodato:str,max:bool):
	lista=[]
	if tipodato=='temperatura(C)':
		if max==True:
			dato=tmpmax(dicc)
		else:
			dato=tmpmin(dicc)
	if tipodato=='Velocidad_viento':
		if max==True:
			dato=velmax(dicc)
		else:
			dato=velmin(dicc)
	for ciudad,datos in dicc.items():
		if datos[tipodato]==dato:
			lista.append(ciudad)
	return lista
