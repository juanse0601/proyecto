import sys
diccionario={}
datos={'fecha':0,'hora':0,'condicion del cielo':0,'visibilidad':0,'temperatura(C°)':0,'Sensacion termica(C°)':0,'Humedad':0,'Viento':0,'Presion':0}
lista=['ciudad/estacion','fecha','hora','condicion del cielo','visibilidad','temperatura(C°)','Sensacion termica(C°)','Humedad','Viento','Presion']
with open(sys.argv[1]) as f:
	for fila in f:
		for i in range(1,10):
			datos[lista[i]]=fila.split(';')[i]
		diccionario[fila.split(';')[0]]=datos



