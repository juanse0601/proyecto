import sys
import datetime
def cargar(ruta: str) -> dict:		
	diccionario={}
	with open(ruta,encoding='cp1252') as f:
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
			print(datos['fecha y hora'])
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
    
if __name__ =='__main__':
	diccionario=cargar(sys.argv[1])
