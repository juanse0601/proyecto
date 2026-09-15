import sys
def cargar(ruta: str) -> dict:		
	diccionario={}
	with open(ruta) as f:
		for fila in f:
			elementos=fila.strip().split(';')
			datos={
			'fecha':elementos[1],
			'hora':elementos[2],
			'condicion del cielo':elementos[3],
			'visibilidad':elementos[4],
			'temperatura(C°)':elementos[5],
			'Sensacion termica(C°)':elementos[6],
			'Humedad':elementos[7],
			'Direccion_viento':'',
			'Velocidad_viento':0,
			'Presion':elementos[9]
			}
			viento = elementos[8].strip()
			if viento.lower()=='calma':
				datos['Direccion_viento']='Calma'
				datos['Velocidad_viento']=0
			else:
				dirvel=viento.split()
				datos.update({
				'Direccion_viento':dirvel[0],
				'Velocidad_viento':dirvel[1]
				})
			diccionario[elementos[0]] = datos
		return(diccionario)
if __name__ =='__main__':
	diccionario=cargar(sys.argv[1])
	print(diccionario['Azul'])
