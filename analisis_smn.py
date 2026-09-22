import sys
import datetime
from cargardicc import cargar
from ciudades import nombre_ciudades
from ciudadescompletas import estacompleto
import tmpmaxmin
diccionario=cargar(sys.argv[1])
largodicc=len(diccionario)
lista=['ciudad/estacion','fecha','hora','condicion del cielo','visibilidad','temperatura(C)','Sensacion termica(C)','Humedad','Direccion_viento','Velocidad_viento','Presion']


tmpmaxmin.topciudades(diccionario,'Velocidad_viento',5,False)


