import sys
import datetime
from funciones_smn import tipo_encoding


def cantidad_ciudades_completas(dicc:dict) -> int:
	contador=0
	for ciudad,datos in dicc.items():
		if datos['Sensacion termica(C)'] != 'No se calcula' and not "" in datos.values():
			contador=contador+1
	return contador		

def listaciudadescompletas(dicc:dict) -> list:
	lista=[]
	for ciudad,datos in dicc.items():
		if datos['Sensacion termica(C)'] != 'No se calcula' and not "" in datos.values():
			lista.append(ciudad)
	return lista
##Funciones para cargar diccionario
def leer_observaciones(ruta: str) -> dict:		
	diccionario={}
	try:
		tipoencoding=tipo_encoding(ruta)
		print('Tipo de encoding:',tipoencoding)
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
				##Verificamos si viento en calma o variable
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
					datos['Direccion_viento']=dirvel[0]
					try:
						datos['Velocidad_viento'] = float(dirvel[1])
					except ValueError:
						datos['Velocidad_viento'] = 0.0
					
				diccionario[elementos[0]] = datos
			return(diccionario)
	except Exception as e:
		print('Ocurrio error', e)
		
##Convertir mes en fecha numerica
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
    
##Lista con nombres de las ciudades
def listaciudades(dicc: dict) -> list:
	lista=[]
	for ciudad,datos in dicc.items():
		lista.append(ciudad)
		
	return lista
#Devuelve las n ciudades con mayor o menor tipodato
def top_n_ciudades(dicc:dict, tipodato:str, n:int, descendente:bool) ->list:
	lista=[(datos[tipodato],ciudad) for ciudad, datos in dicc.items()]
	if descendente==True:
		lista.sort(reverse=True)
	else:
		lista.sort(reverse=False)
	return lista[:n]

#Devuelve la mayor o menor tipo de dato	
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
	
#Devuelve lista con ciudades con la mayor o menor de tipo de dato
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
	
def leerdatos(diccionario:dict ):
	nombres_ciudades=listaciudades(diccionario)
	print('Pruebas:\n')
	print('Ejemplo de datos de la ciudad Azul',diccionario[nombres_ciudades[0]])
	print(f'\nHay {cantidad_ciudades_completas(diccionario)} ciudades completas:',listaciudadescompletas(diccionario))
	#n ciudades
	print('\n5 ciudades con mayor velocidad de viento:',top_n_ciudades(diccionario,'Velocidad_viento',5,True))
	print('\n5 ciudades con menor temperatura:',top_n_ciudades(diccionario,'temperatura(C)',5,False))
	#Velocidad max
	print('\nVelocidad max:',maxmin(diccionario,'Velocidad_viento',True))
	print('Ciudades con max velocidad viento:',ciudades(diccionario,'Velocidad_viento',True))
	##Velocidad min
	print('\nVelocidad min:',maxmin(diccionario,'Velocidad_viento',False))
	print('Ciudades con min velocidad viento:',ciudades(diccionario,'Velocidad_viento',False))
	#Tmp max 
	print('\nTemperatura max:',maxmin(diccionario,'temperatura(C)',True))
	print('Ciudad(es) con max temperatura:',ciudades(diccionario,'temperatura(C)',True))
	#Tmp min
	print('\nTemperatura min:',maxmin(diccionario,'temperatura(C)',False))
	print('Ciudad(es) con min temperatura:',ciudades(diccionario,'temperatura(C)',False))

    
if __name__ =='__main__':
	diccionario=leer_observaciones(sys.argv[1])
	leerdatos(diccionario)
