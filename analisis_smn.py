import sys
import datetime
import funciones

def leerdatos(diccionario:dict ):
	print('Pruebas:\n')
	print('Ejemplo de datos de la ciudad Azul',diccionario['Azul'])
	print(f'\nHay {funciones.estacompleto(diccionario)} ciudades completas:',funciones.listaciudadescompletas(diccionario))
	
	print('\n5 ciudades con mayor velocidad de viento:',funciones.topciudades(diccionario,'Velocidad_viento',5,True))
	print('\n7 ciudades con menor temperatura:',funciones.topciudades(diccionario,'temperatura(C)',7,False))
	#Velocidad max
	print('\nVelocidad max:',funciones.maxmin(diccionario,'Velocidad_viento',True))
	print('Ciudades con max velocidad viento:',funciones.ciudades(diccionario,'Velocidad_viento',True))
	##Velocidad min
	print('\nVelocidad min:',funciones.maxmin(diccionario,'Velocidad_viento',False))
	print('Ciudades con min velocidad viento:',funciones.ciudades(diccionario,'Velocidad_viento',False))
	#Tmp max 
	print('\nTemperatura max:',funciones.maxmin(diccionario,'temperatura(C)',True))
	print('Ciudad(es) con max temperatura:',funciones.ciudades(diccionario,'temperatura(C)',True))
	#Tmp min
	print('\nTemperatura min:',funciones.maxmin(diccionario,'temperatura(C)',False))
	print('Ciudad(es) con min temperatura:',funciones.ciudades(diccionario,'temperatura(C)',False))

diccionario=funciones.cargar(sys.argv[1])
largodicc=len(diccionario)
lista=['ciudad/estacion','fecha','hora','condicion del cielo','visibilidad','temperatura(C)','Sensacion termica(C)','Humedad','Direccion_viento','Velocidad_viento','Presion']
leerdatos(diccionario)
