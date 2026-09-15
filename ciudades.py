import sys
def nombre_ciudades(ruta: str) -> list:		
	lista=[]
	with open(ruta) as f:
		for fila in f:
			elementos=fila.strip().split(';')
			lista.append(elementos[0])
	return(lista)
if __name__ =='__main__':
	lista=nombreciudades(sys.argv[1])
	print(lista)
