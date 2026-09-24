import sys
import datetime
from cargardicc import cargar
from ciudadescompletas import estacompleto, listaciudadescompletas
import tmpmaxmin

def leerdatos(diccionario:dict ):
	print('Pruebas:')
	print('Ejemplo de datos de la ciudad Azul',diccionario['Azul'])
	print(f'Hay {estacompleto(diccionario)} ciudades completas:',listaciudadescompletas(diccionario))
	print(' 5 ciudades con mayor velocidad de viento:',tmpmaxmin.topciudades(diccionario,'Velocidad_viento',5,True))
	print(' 7 ciudades con menor temperatura:',tmpmaxmin.topciudades(diccionario,'temperatura(C)',7,False))
	#Velocidad max
	print('Velocidad max:',tmpmaxmin.velmax(diccionario))
	print('Ciudades con max velocidad viento:',tmpmaxmin.ciudades(diccionario,'Velocidad_viento',True))
	##Velocidad min
	print('Velocidad min:',tmpmaxmin.velmin(diccionario))
	print('Ciudades con min velocidad viento:',tmpmaxmin.ciudades(diccionario,'Velocidad_viento',False))
	#Tmp max 
	print('Temperatura max:',tmpmaxmin.tmpmax(diccionario))
	print('Ciudad(es) con max temperatura:',tmpmaxmin.ciudades(diccionario,'temperatura(C)',True))
	#Tmp min
	print('Temperatura min:',tmpmaxmin.tmpmin(diccionario))
	print('Ciudad(es) con min temperatura:',tmpmaxmin.ciudades(diccionario,'temperatura(C)',False))

diccionario=cargar(sys.argv[1])
largodicc=len(diccionario)
lista=['ciudad/estacion','fecha','hora','condicion del cielo','visibilidad','temperatura(C)','Sensacion termica(C)','Humedad','Direccion_viento','Velocidad_viento','Presion']
leerdatos(diccionario)
