import sys
from cargardicc import cargar
from ciudades import nombre_ciudades
from ciudadescompletas import estacompleto
diccionario=cargar(sys.argv[1])
nombres=nombre_ciudades(sys.argv[1])
lista=['ciudad/estacion','fecha','hora','condicion del cielo','visibilidad','temperatura(C°)','Sensacion termica(C°)','Humedad','Viento','Presion']
print(estacompleto(diccionario))


