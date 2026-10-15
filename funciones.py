import sys
import datetime
from funcionesjson import tipo_encoding

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
#############################
def cargar(ruta: str) -> dict:		
	diccionario={}
	tipoencoding=tipo_encoding(ruta)
	print('Tipo de encoding:',tipoencoding)
	try:
		with open(ruta,encoding=tipoencoding) as f:
			for fila in f:
				elementos=fila.strip().split(';')
				fechas=convertir_fecha(elementos[1],elementos[2])
				fechadatetime=datetime.datetime.strptime(fechas,"%d-%m-%Y %H:%M")
				datos={
				'fecha y hora':fechadatetime,
				'condicion del cielo':elementos[3],
				'visibilidad':elementos[4],
				'temperatura(C)':float(elementos[5]),
				'Sensacion termica(C)':elementos[6],
				'Humedad':elementos[7],
				'Direccion_viento':'',
				'Velocidad_viento':0.0,
				'Presion':elementos[9]
				}
				viento = elementos[8].strip()
				if viento.lower()=='calma':
					datos['Direccion_viento']='Calma'
					datos['Velocidad_viento']=0.0
				elif viento.lower()=='direcciones variables':
					dirvel=viento.split( )
					datos['Direccion_viento']='Variable'
					datos['Velocidad_viento']=float(dirvel[1])
					
				else:
					dirvel=viento.split( )
					datos['Direccion_viento']=dirvel[0],
					try:
						datos['Velocidad_viento'] = float(dirvel[1])
					except ValueError:
						datos['Velocidad_viento'] = 0.0
					
				diccionario[elementos[0]] = datos
			return(diccionario)
	except Exception as e:
		print('Ocurrio error', e)
		
def convertir_fecha(fecha,hora):
    meses = {
        'enero': '01',
        'febrero': '02',
        'marzo': '03',
        'abril': '04',
        'mayo': '05',
        'junio': '06',
        'julio': '07',
        'agosto': '08',
        'septiembre': '09',
        'octubre': '10',
        'noviembre': '11',
        'diciembre': '12'
    }
    dia, mes, anio =fecha.lower().split('-')
    hora,minuto =hora.split(':')
    fecha_numerica = f'{dia}-{meses[mes]}-{anio} {hora}:{minuto}'
    return fecha_numerica 
def listaciudades(dicc: dict) -> list:
	lista=[]
	for ciudad,datos in dicc.items():
		lista.append(ciudad)
		
	return lista
########################    
def topciudades(dicc:dict, tipodato:str, n:int, descendente:bool) ->list:
	lista=[(datos[tipodato],ciudad) for ciudad, datos in dicc.items()]
	if descendente==True:
		lista.sort(reverse=True)
	else:
		lista.sort(reverse=False)
	return lista[:n]
	
def maxmin(dicc:dict,tipodato:str,max:bool) -> float:
	ciudades=listaciudades(dicc)
	salida=dicc[ciudades[0]][tipodato]
	if max:
		for ciudad,datos in dicc.items():
			if datos[tipodato] > salida:
				salida=datos[tipodato]
	else:
		for ciudad,datos in dicc.items():
			if datos[tipodato] < salida:
				salida=datos[tipodato]					
	return salida
	

def ciudades(dicc:dict,tipodato:str,max:bool):
	lista=[]
	if tipodato=='temperatura(C)':
		if max==True:
			dato=maxmin(dicc,tipodato,max)
		else:
			dato=maxmin(dicc,tipodato,max)
	if tipodato=='Velocidad_viento':
		if max==True:
			dato=maxmin(dicc,tipodato,max)
		else:
			dato=maxmin(dicc,tipodato,max)
	for ciudad,datos in dicc.items():
		if datos[tipodato]==dato:
			lista.append(ciudad)
	return lista

    
if __name__ =='__main__':
	diccionario=cargar(sys.argv[1])
